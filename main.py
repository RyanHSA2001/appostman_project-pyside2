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

from Custom_Widgets.Widgets import *

class UtilityFunctions:

    def open_message_box(self, icon, title, message, parent=None, ok_and_cancel=False):
        msg_box = QMessageBox(parent)
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        font = QFont("Palatino Linotype", 12)
        msg_box.setFont(font)

        if ok_and_cancel:
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg_box.exec()

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

                user_id = db.select_last_user_id()
                with SystemDataBase(name='user_' + str(user_id) + '.db') as sdb:
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
                    self.main_window = MainWindow()
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
    def __init__(self):
        super(MainWindow, self).__init__()

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

if __name__ == "__main__":
    with LoginDataBase() as db:
        db.setup_database()

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
