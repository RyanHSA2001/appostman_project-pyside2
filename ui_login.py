# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(444, 574)
        Login.setMaximumSize(QSize(444, 639))
        icon = QIcon()
        icon.addFile(u"resources/mail.png", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_principal = QFrame(Login)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setStyleSheet(u"background-color: rgb(233, 242, 249);")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_principal)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_esquerda = QFrame(self.frame_principal)
        self.frame_esquerda.setObjectName(u"frame_esquerda")
        self.frame_esquerda.setMinimumSize(QSize(0, 0))
        self.frame_esquerda.setMaximumSize(QSize(444, 16777215))
        self.frame_esquerda.setFrameShape(QFrame.StyledPanel)
        self.frame_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_esquerda)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, 0)
        self.label_3 = QLabel(self.frame_esquerda)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 80))
        self.label_3.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setFamily(u"Rockwell")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(27, 50, 95);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame_esquerda)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(Qt.StrongFocus)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit_login_username = QLineEdit(self.frame_esquerda)
        self.lineEdit_login_username.setObjectName(u"lineEdit_login_username")
        self.lineEdit_login_username.setMinimumSize(QSize(300, 30))
        self.lineEdit_login_username.setMaximumSize(QSize(300, 35))
        font1 = QFont()
        font1.setFamily(u"Palatino Linotype")
        font1.setPointSize(14)
        font1.setItalic(False)
        self.lineEdit_login_username.setFont(font1)
        self.lineEdit_login_username.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(199, 206, 211);\n"
"}")
        self.lineEdit_login_username.setFrame(False)
        self.lineEdit_login_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEdit_login_username, 0, Qt.AlignHCenter)

        self.lineEdit_login_password = QLineEdit(self.frame_esquerda)
        self.lineEdit_login_password.setObjectName(u"lineEdit_login_password")
        self.lineEdit_login_password.setMinimumSize(QSize(300, 35))
        self.lineEdit_login_password.setMaximumSize(QSize(300, 35))
        self.lineEdit_login_password.setFont(font1)
        self.lineEdit_login_password.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(199, 206, 211);\n"
"}")
        self.lineEdit_login_password.setMaxLength(30)
        self.lineEdit_login_password.setFrame(False)
        self.lineEdit_login_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_login_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEdit_login_password, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.frame_esquerda)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_login = QPushButton(self.frame)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setMinimumSize(QSize(100, 40))
        font2 = QFont()
        font2.setFamily(u"Palatino Linotype")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.pushButton_login.setFont(font2)
        self.pushButton_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_login.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(158, 195, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"color: rgb(0, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"resources/circle-right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_login.setIcon(icon1)
        self.pushButton_login.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_login, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_esquerda)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 180))
        self.frame_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_redefine_password = QPushButton(self.frame_2)
        self.pushButton_redefine_password.setObjectName(u"pushButton_redefine_password")
        self.pushButton_redefine_password.setMinimumSize(QSize(170, 35))
        self.pushButton_redefine_password.setMaximumSize(QSize(170, 35))
        font3 = QFont()
        font3.setFamily(u"Rockwell")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.pushButton_redefine_password.setFont(font3)
        self.pushButton_redefine_password.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_redefine_password.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(58, 137, 201);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: rgb(156, 196, 228);\n"
"}")
        self.pushButton_redefine_password.setFlat(False)

        self.verticalLayout_4.addWidget(self.pushButton_redefine_password, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pushButton_newuser = QPushButton(self.frame_2)
        self.pushButton_newuser.setObjectName(u"pushButton_newuser")
        self.pushButton_newuser.setMinimumSize(QSize(170, 35))
        self.pushButton_newuser.setMaximumSize(QSize(300, 35))
        self.pushButton_newuser.setFont(font3)
        self.pushButton_newuser.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_newuser.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(58, 137, 201);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: rgb(156, 196, 228);\n"
"}")

        self.verticalLayout_4.addWidget(self.pushButton_newuser, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamily(u"Rockwell")
        font4.setPointSize(10)
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame_esquerda)

        self.frame_direita = QFrame(self.frame_principal)
        self.frame_direita.setObjectName(u"frame_direita")
        self.frame_direita.setMaximumSize(QSize(0, 16777215))
        self.frame_direita.setFrameShape(QFrame.StyledPanel)
        self.frame_direita.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_direita)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.label_4 = QLabel(self.frame_direita)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 80))
        font5 = QFont()
        font5.setFamily(u"Rockwell")
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(27, 50, 95);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label = QLabel(self.frame_direita)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 80))
        font6 = QFont()
        font6.setFamily(u"Rockwell")
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.label.setFont(font6)
        self.label.setFocusPolicy(Qt.StrongFocus)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.lineEdit_signup_username = QLineEdit(self.frame_direita)
        self.lineEdit_signup_username.setObjectName(u"lineEdit_signup_username")
        self.lineEdit_signup_username.setMinimumSize(QSize(300, 30))
        self.lineEdit_signup_username.setMaximumSize(QSize(300, 35))
        font7 = QFont()
        font7.setFamily(u"Palatino Linotype")
        font7.setPointSize(12)
        font7.setItalic(False)
        self.lineEdit_signup_username.setFont(font7)
        self.lineEdit_signup_username.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(199, 206, 211);\n"
"}")
        self.lineEdit_signup_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_signup_username, 0, Qt.AlignHCenter)

        self.lineEdit_signup_email = QLineEdit(self.frame_direita)
        self.lineEdit_signup_email.setObjectName(u"lineEdit_signup_email")
        self.lineEdit_signup_email.setMinimumSize(QSize(300, 30))
        self.lineEdit_signup_email.setMaximumSize(QSize(300, 35))
        self.lineEdit_signup_email.setFont(font7)
        self.lineEdit_signup_email.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(199, 206, 211);\n"
"}")
        self.lineEdit_signup_email.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_signup_email, 0, Qt.AlignHCenter)

        self.lineEdit_signup_password = QLineEdit(self.frame_direita)
        self.lineEdit_signup_password.setObjectName(u"lineEdit_signup_password")
        self.lineEdit_signup_password.setMinimumSize(QSize(300, 30))
        self.lineEdit_signup_password.setMaximumSize(QSize(300, 35))
        self.lineEdit_signup_password.setFont(font7)
        self.lineEdit_signup_password.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(199, 206, 211);\n"
"}")
        self.lineEdit_signup_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_signup_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_signup_password, 0, Qt.AlignHCenter)

        self.lineEdit_signup_repeat_password = QLineEdit(self.frame_direita)
        self.lineEdit_signup_repeat_password.setObjectName(u"lineEdit_signup_repeat_password")
        self.lineEdit_signup_repeat_password.setMinimumSize(QSize(300, 30))
        self.lineEdit_signup_repeat_password.setMaximumSize(QSize(300, 35))
        self.lineEdit_signup_repeat_password.setFont(font7)
        self.lineEdit_signup_repeat_password.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(199, 206, 211);\n"
"}")
        self.lineEdit_signup_repeat_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_signup_repeat_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_signup_repeat_password, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame_direita)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(61, -1, -1, -1)
        self.checkBox_receive_emails = QCheckBox(self.frame_3)
        self.checkBox_receive_emails.setObjectName(u"checkBox_receive_emails")
        font8 = QFont()
        font8.setFamily(u"Palatino Linotype")
        font8.setPointSize(11)
        self.checkBox_receive_emails.setFont(font8)
        self.checkBox_receive_emails.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.checkBox_receive_emails)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame_direita)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_signup = QPushButton(self.frame_5)
        self.pushButton_signup.setObjectName(u"pushButton_signup")
        self.pushButton_signup.setMinimumSize(QSize(150, 40))
        self.pushButton_signup.setMaximumSize(QSize(100, 40))
        font9 = QFont()
        font9.setFamily(u"Palatino Linotype")
        font9.setPointSize(14)
        self.pushButton_signup.setFont(font9)
        self.pushButton_signup.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_signup.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(158, 195, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"color: rgb(0, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"resources/add-contact.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_signup.setIcon(icon2)
        self.pushButton_signup.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.pushButton_signup)


        self.verticalLayout_3.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame_direita)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_goback = QPushButton(self.frame_4)
        self.pushButton_goback.setObjectName(u"pushButton_goback")
        self.pushButton_goback.setMinimumSize(QSize(170, 35))
        self.pushButton_goback.setMaximumSize(QSize(300, 35))
        self.pushButton_goback.setFont(font3)
        self.pushButton_goback.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goback.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(58, 137, 201);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: rgb(156, 196, 228);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_goback, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_direita)


        self.verticalLayout.addWidget(self.frame_principal)

        QWidget.setTabOrder(self.label_2, self.lineEdit_login_username)
        QWidget.setTabOrder(self.lineEdit_login_username, self.lineEdit_login_password)
        QWidget.setTabOrder(self.lineEdit_login_password, self.lineEdit_signup_username)
        QWidget.setTabOrder(self.lineEdit_signup_username, self.lineEdit_signup_email)
        QWidget.setTabOrder(self.lineEdit_signup_email, self.lineEdit_signup_password)
        QWidget.setTabOrder(self.lineEdit_signup_password, self.lineEdit_signup_repeat_password)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Bem vindo ao Appostman", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Fazer login", None))
        self.lineEdit_login_username.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.lineEdit_login_password.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.pushButton_login.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.pushButton_redefine_password.setText(QCoreApplication.translate("Login", u"Esqueceu a senha?", None))
        self.pushButton_newuser.setText(QCoreApplication.translate("Login", u"Ainda n\u00e3o possui uma conta?", None))
        self.label_5.setText(QCoreApplication.translate("Login", u"Vers\u00e3o 1.0/2023", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"Seu software de e-mail marketing!", None))
        self.label.setText(QCoreApplication.translate("Login", u"Criar conta", None))
        self.lineEdit_signup_username.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.lineEdit_signup_email.setPlaceholderText(QCoreApplication.translate("Login", u"E-mail", None))
        self.lineEdit_signup_password.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.lineEdit_signup_repeat_password.setPlaceholderText(QCoreApplication.translate("Login", u"Digite a senha novamente", None))
        self.checkBox_receive_emails.setText(QCoreApplication.translate("Login", u"Aceito receber e-mails informativos", None))
        self.pushButton_signup.setText(QCoreApplication.translate("Login", u"Cadastrar-se", None))
        self.pushButton_goback.setText(QCoreApplication.translate("Login", u"Voltar ao Login", None))
    # retranslateUi

