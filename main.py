from ui_login import Ui_Login
from ui_main import Ui_MainWindow

from database import LoginDataBase, SystemDataBase

from PySide2.QtWidgets import QWidget, QMainWindow, QMessageBox, QApplication
from PySide2.QtCore import QEasingCurve, QPropertyAnimation, Qt
from PySide2.QtGui import QFont

import hashlib
import re
import sys
import csv
import styles
import webbrowser
import os
import shutil

from Custom_Widgets.Widgets import *

class UtilityFunctions:

    def able_disable_buttons(self, button, able:bool, stylesheet):
        button.setEnabled(able)
        button.setStyleSheet(stylesheet)

    def open_message_box(self, icon, title, message, parent=None, ok_and_cancel=False):
        self.msg_box = QMessageBox(parent)
        self.msg_box.setIcon(icon)
        self.msg_box.setWindowTitle(title)
        self.msg_box.setText(message)
        font = QFont("Palatino Linotype", 12)
        self.msg_box.setFont(font)

        if ok_and_cancel:
            self.msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        return self.msg_box.exec()

    def validate_email(self, email):
        standard = r'^[\w]+[\.\w-]*@[\w-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2})?$'

        if re.match(standard, email):
            return True
        return False

    def password_to_hash(self, password):
        hash_obj = hashlib.md5()
        user_password = password
        bytes_password = user_password.encode("UTF-8")
        hash_obj.update(bytes_password)
        password_hash = hash_obj.hexdigest()
        return password_hash

class Login(QWidget, Ui_Login, UtilityFunctions):
    def __init__(self):
        super(Login, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Appostman- Login")

        self.shortcut = 0

        # Eventos tela de login
        self.pushButton_newuser.clicked.connect(self.signup_screen_animation)
        self.pushButton_goback.clicked.connect(self.signup_screen_animation)
        self.pushButton_signup.clicked.connect(self.insert_user)
        self.pushButton_login.clicked.connect(self.check_login)

        self.lineEdit_login_username.returnPressed.connect(self.check_login)
        self.lineEdit_login_password.returnPressed.connect(self.check_login)

        # Eventos tela de cadastro
        self.lineEdit_signup_username.returnPressed.connect(self.check_login)
        self.lineEdit_signup_email.returnPressed.connect(self.check_login)
        self.lineEdit_signup_password.returnPressed.connect(self.check_login)
        self.lineEdit_signup_repeat_password.returnPressed.connect(self.check_login)

    def signup_screen_animation(self):
        """
        Executa a animação de transição da tela de login para cadastro.
        Abre um frame e fecha o outro.
        """
        frame_direita_width = self.frame_direita.width()

        if frame_direita_width == 0:
            newWidth = 444
        else:
            newWidth = 0

        self.right_animation = QPropertyAnimation(self.frame_direita, b"maximumWidth")
        self.right_animation.setDuration(200)
        self.right_animation.setStartValue(frame_direita_width)
        self.right_animation.setEndValue(newWidth)
        self.right_animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.right_animation.start()

        frame_esquerda_width = self.frame_esquerda.width()

        if frame_esquerda_width == 0:
            newWidth = 444
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self.frame_esquerda, b"maximumWidth")
        self.animation.setDuration(200)
        self.animation.setStartValue(frame_esquerda_width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def insert_user(self):
        username = self.lineEdit_signup_username.text()
        password = self.lineEdit_signup_password.text()
        email = self.lineEdit_signup_email.text()
        repeat_password = self.lineEdit_signup_repeat_password.text()
        if self.checkBox_receive_emails.isChecked():
            accept_emails = 1
        else:
            accept_emails = 0
        password_hash = self.password_to_hash(password)

        if (not username
                or not password
                or not email
                or not repeat_password):
            self.open_message_box(QMessageBox.Warning, "Erro", "Todos os campos devem ser preenchidos.", self)
            return

        if not self.validate_email(email):
            self.open_message_box(QMessageBox.Warning, "Erro", "Formato de e-mail inválido", self)
            return

        if password != repeat_password:
            self.open_message_box(QMessageBox.Warning, "Erro", "As senhas divergem.", self)
            return

        with LoginDataBase() as db:
            if db.insert_user(username, password_hash, email, accept_emails):

                self.user_id = db.select_last_user_id()
                with SystemDataBase(name='user_' + str(self.user_id) + '.db') as sdb:
                    sdb.setup_database()

                self.open_message_box(QMessageBox.Information, "Sucesso", "Cadastro realizado com sucesso!", self)
                self.lineEdit_signup_username.setText("")
                self.lineEdit_signup_password.setText("")
                self.lineEdit_signup_email.setText("")
                self.lineEdit_signup_repeat_password.setText("")
                return True

            self.open_message_box(QMessageBox.Warning, "Erro", "Erro na inserção: nome de usuário ou e-mail já cadastrado.", self)

            return False

    def check_login(self):
        username = self.lineEdit_login_username.text()
        password = self.lineEdit_login_password.text()

        password_hash = self.password_to_hash(password)

        if not username or not password:
            self.open_message_box(QMessageBox.Warning, "Erro", "Todos os campos devem ser preenchidos.", self)
            return

        with LoginDataBase() as db:
                if db.check_login(username, password_hash):
                    self.user_id = db.check_logged_user_id(username, password_hash)
                    self.main_window = MainWindow(self.user_id)
                    self.main_window.show()
                    self.close()
                    return

                self.open_message_box(QMessageBox.Warning, "Erro", "Usuário ou senha inválidos.", self)
                return

    def switch_shortcut(self):
        if self.shortcut:
            self.pushButton_login.setShortcut('')
            self.pushButton_signup.setShortcut('Enter')
            return
        else:
            self.pushButton_signup.setShortcut('')
            self.pushButton_login.setShortcut('Enter')

class MainWindow(QMainWindow, Ui_MainWindow, UtilityFunctions):
    def __init__(self, user_id):
        super(MainWindow, self).__init__()

        self.logged_user_db = "user_" + str(user_id) + ".db"
        self.messages_folder = "messages"
        os.makedirs(self.messages_folder, exist_ok=True)
        self.setupUi(self)
        self.setWindowTitle("Appostman")
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.window_size = 0


        def moveWindow(e):

            if self.isMaximized() == False:

                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        # Eventos de navegação
        self.button_dashboard.clicked.connect(lambda: self.pages.setCurrentWidget(self.dashboard))
        self.button_recipients.clicked.connect(lambda: self.pages.setCurrentWidget(self.recipients))
        self.button_messages.clicked.connect(lambda: self.pages.setCurrentWidget(self.messages))
        self.button_configurations.clicked.connect(lambda: self.pages.setCurrentWidget(self.configurations))
        self.button_help.clicked.connect(lambda: self.pages.setCurrentWidget(self.help))
        self.button_about.clicked.connect(lambda: self.pages.setCurrentWidget(self.about))

        # Eventos tela principal
        self.button_menu.clicked.connect(self.left_menu_animation)
        self.header_central_frame.mouseMoveEvent = moveWindow
        self.button_restore.clicked.connect(self.restore_or_maximize_window)
        self.button_minimize.clicked.connect(lambda: self.showMinimized())
        self.button_close.clicked.connect(lambda: self.close())

        # Eventos tela de destinatários
        self.button_search_recipients.clicked.connect(self.open_recipients_file_dialog)
        self.button_validar.clicked.connect(self.validate_recipients)
        self.button_cadastrar.clicked.connect(self.upload_recipients)
        horizontal_header = self.table_recipients.horizontalHeader()
        horizontal_header.setStyleSheet(styles.horizontal_header_style)
        horizontal_header.setSectionResizeMode(0, QHeaderView.Stretch)
        horizontal_header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.table_recipients.verticalHeader().setVisible(False)
        self.show_recipients()

        # Eventos tela de mensagens

        self.button_search_message.clicked.connect(self.open_message_file_dialog)
        self.button_validar_message.clicked.connect(self.validate_html)
        self.button_cadastrar_message.clicked.connect(self.upload_message)
        self.button_cadastrar_message.clicked.connect(self.refresh_message_list)
        self.show_messages()
        self.button_excluir_message.clicked.connect(self.delete_item)
        self.listWidget_message.itemDoubleClicked.connect(self.validate_html_by_double_click)

        # Eventos tela de configurações

        self.tabWidget.tabBar().setCursor(QtCore.Qt.PointingHandCursor)

    def restore_or_maximize_window(self):
        if self.window_size == 0:
            self.window_size = 1
            self.showMaximized()
            self.button_restore.setIcon(QtGui.QIcon(u"resources/main-window-icons/minimize.png"))
        else:
            self.window_size = 0
            self.showNormal()
            self.button_restore.setIcon(QtGui.QIcon(u"resources/main-window-icons/maximize.png"))

    # Evento de interação com barra de titulo
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def left_menu_animation(self):
        #  ABRE O MENU LATERAL ESQUERDO DE FORMA ANIMADA
        width = self.left_menu_frame.width()

        if width == 0:
            newWidth = 250
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self.left_menu_frame, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    # Funções tela de destinatários
    def open_recipients_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Valores Separados por Vírgula (*.csv)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            self.label_file_path_recipients.setText(file_name)
            self.able_disable_buttons(self.button_validar, True, styles.light_yellow_button)
            self.recipients_filename = file_name
        else:
            self.label_file_path_recipients.setText("Selecione um arquivo")
            self.able_disable_buttons(self.button_validar, False, styles.disabled_gray_button)

        self.able_disable_buttons(self.button_cadastrar, False, styles.disabled_gray_button)

    def get_contacts(self, filename) -> tuple:
        names = []
        emails = []
        ages = []
        sexes = []
        country_codes = []
        with open(filename, mode='r', encoding='utf-8') as recipients_file:
            index = 0
            for a_recipient in recipients_file:
                index += 1
                names.append(a_recipient.split(',')[0].replace('\n', ''))

                email = a_recipient.split(',')[1].replace('\n', '')

                if self.validate_email(email):
                    emails.append(email)
                else:
                    error_message = f"Encontrado um e-mail inválido na linha {index}, por favor corrija o " \
                                    "arquivo e tente novamente."
                    self.open_message_box(QMessageBox.Warning, "Erro", error_message, self)
                    return
                ages.append(a_recipient.split(',')[2].replace('\n', ''))
                sexes.append(a_recipient.split(',')[3].replace('\n', ''))
                country_codes.append(a_recipient.split(',')[4].replace('\n', ''))

            return names, emails, ages, sexes, country_codes

    def validate_recipients(self):
        try:
            self.names, self.emails, self.ages, self.sexes, self.country_codes = self.get_contacts(
                self.recipients_filename)

            if len(self.names) == len(self.emails) and len(self.emails) == len(self.ages):
                success_message = f"Arquivo válido.\nForam encontrados {len(self.emails)} contatos válidos."
                self.open_message_box(QMessageBox.Information, "Sucesso", success_message, self)
                self.able_disable_buttons(self.button_cadastrar, True, styles.light_green_button)
            else:
                self.open_message_box(QMessageBox.Warning, "Erro", "Erro desconhecido na leitura do arquivo", self)

        except(IndexError, UnicodeDecodeError):
            self.open_message_box(QMessageBox.Warning, "Erro", "Arquivo inválido. Consulte o menu AJUDA para uma "
                                                               "explicação do leiaute do arquivo.", self)
        except ValueError as e:
            self.open_message_box(QMessageBox.Warning, "Erro", str(e), self)

    def upload_recipients(self):
        try:
            with SystemDataBase(self.logged_user_db) as db:
                for i, name in enumerate(self.names):
                    db.insert_recipient(name, self.emails[i], self.ages[i], self.sexes[i], self.country_codes[i])

                self.open_message_box(QMessageBox.Information, "Sucesso", "Destinatários cadastrados com "
                                                                          "sucesso!", self)

                self.label_file_path_recipients.setText("Selecione um arquivo")
                self.able_disable_buttons(self.button_validar, False, styles.disabled_gray_button)
                self.able_disable_buttons(self.button_cadastrar, False, styles.disabled_gray_button)
            self.show_recipients()

        except Exception as e:
            self.open_message_box(QMessageBox.Warning, "Erro", str(e), self)

    def show_recipients(self):
        with SystemDataBase(self.logged_user_db) as db:
            result = db.select_recipients()

        row = 0
        self.table_recipients.setRowCount(len(result))
        for recipient in result:
            item1 = QTableWidgetItem(recipient[0])
            item2 = QTableWidgetItem(recipient[1])

            font = QFont("Rockwell", 12)
            item1.setFont(font)
            item2.setFont(font)

            item1.setFlags(item1.flags() ^ Qt.ItemIsEditable)
            item2.setFlags(item2.flags() ^ Qt.ItemIsEditable)

            self.table_recipients.setItem(row, 0, item1)
            self.table_recipients.setItem(row, 1, item2)

            row +=1

            self.label_recipients.setText(f"Destinatários Encontrados: {row}")

    # Funções tela de mensagens

    def open_message_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("HyperText Markup Language (*.html)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            self.label_file_path_message.setText(file_path)
            self.able_disable_buttons(self.button_validar_message, True, styles.light_yellow_button)
            self.able_disable_buttons(self.lineEdit_message_name, True, styles.line_edit_style)
            self.able_disable_buttons(self.button_cadastrar_message, True, styles.light_green_button)

            self.message_filename = os.path.basename(file_path)
            self.message_original_filepath = file_path
        else:
            self.label_file_path_message.setText("Selecione um arquivo")
            self.able_disable_buttons(self.button_validar_message, False, styles.disabled_gray_button)
            self.able_disable_buttons(self.lineEdit_message_name, False, styles.line_edit_gray)
            self.able_disable_buttons(self.button_cadastrar, False, styles.disabled_gray_button)
            self.lineEdit_message_name.setText("")

    def validate_html(self):
        webbrowser.open_new_tab(self.message_original_filepath)

    def validate_html_by_double_click(self, item):
        message_name = item.text()
        divided_message_name = message_name.split(" - ", 1)
        message_name = divided_message_name[1]
        result = False

        with SystemDataBase(self.logged_user_db) as db:
            result = db.select_message_byname(message_name)

        if result:
            webbrowser.open_new_tab(result)

    def show_messages(self):
        with SystemDataBase(self.logged_user_db) as db:
            messages = db.select_all_messages()
        for message in messages:
            message_item = str(message[0]) + " - " + message[2]
            self.listWidget_message.addItem(message_item)

    def copy_to_messages_directory(self, file):
        os.makedirs(self.messages_folder, exist_ok=True)
        shutil.copy(file, self.messages_folder)

    def upload_message(self):
        if not self.lineEdit_message_name.text():
            self.open_message_box(QMessageBox.Warning, "Atenção!", "Por favor digite um nome para a mensagem", self)
            return

        with SystemDataBase(self.logged_user_db) as db:
            message_name = self.lineEdit_message_name.text()

            if not db.select_message_byname(message_name):
                self.message_new_filepath = os.path.join(self.messages_folder, self.message_filename)

                existing_message_id = db.select_message_bypath(self.message_new_filepath)
                alert_message = f"Arquivo já importado na mensagem {existing_message_id}, deseja substituí-lo?"

                if existing_message_id:

                    result = self.open_message_box(QMessageBox.Warning, "Atenção!", alert_message,
                                          self, True)

                    if result == QMessageBox.Ok:
                        self.copy_to_messages_directory(self.message_original_filepath)
                        self.message_id = db.insert_message(self.message_new_filepath, message_name)
                        self.open_message_box(QMessageBox.Information, "Sucesso!", "Mensagem cadastrada com sucesso",
                                              self)
                        self.lineEdit_message_name.setText("")
                        self.label_file_path_message.setText("Selecione um arquivo")
                        self.able_disable_buttons(self.button_cadastrar_message, False, styles.disabled_gray_button)
                        self.able_disable_buttons(self.button_validar_message, False, styles.disabled_gray_button)
                        self.able_disable_buttons(self.lineEdit_message_name, False, styles.line_edit_gray)

                        return
                    return

                self.copy_to_messages_directory(self.message_original_filepath)
                self.message_id = db.insert_message(self.message_new_filepath, message_name)
                self.open_message_box(QMessageBox.Information, "Sucesso!", "Mensagem cadastrada com sucesso",
                                      self)
                self.lineEdit_message_name.setText("")
                self.label_file_path_message.setText("Selecione um arquivo")
                self.able_disable_buttons(self.button_cadastrar_message, False, styles.disabled_gray_button)
                self.able_disable_buttons(self.button_validar_message, False, styles.disabled_gray_button)
                self.able_disable_buttons(self.lineEdit_message_name, False, styles.line_edit_gray)
                return
            self.open_message_box(QMessageBox.Warning, "Erro", "Nome já utilizado", self)
            return


        self.able_disable_buttons(self.button_cadastrar_message, False, styles.disabled_gray_button)
        self.able_disable_buttons(self.button_validar_message, False, styles.disabled_gray_button)
        self.able_disable_buttons(self.lineEdit_message_name, False, styles.line_edit_gray)
        self.lineEdit_message_name.setText("")

    def refresh_message_list(self):
        self.listWidget_message.clear()
        self.show_messages()

    def delete_item(self):
        item = self.listWidget_message.currentItem()

        if item:
            message_name = item.text()
            divided_message_name = message_name.split(" - ", 1)
            message_name = divided_message_name[1]

            with SystemDataBase(self.logged_user_db) as db:
                db.delete_message(message_name)

            self.refresh_message_list()
            return



if __name__ == "__main__":
    with LoginDataBase() as db:
        db.setup_database()

    app = QApplication(sys.argv)

    main_window = Login()
    main_window.show()

    sys.exit(app.exec_())
