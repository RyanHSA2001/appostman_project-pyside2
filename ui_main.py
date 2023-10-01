# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1027, 626)
        MainWindow.setMinimumSize(QSize(1027, 626))
        icon = QIcon()
        icon.addFile(u"resources/mail.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(953, 626))
        self.centralwidget.setStyleSheet(u"QWidget\n"
"{\n"
"background-color: rgb(233, 242, 249);\n"
"}\n"
"\n"
"#left_menu_frame QPushButton\n"
"{\n"
"\n"
"opacity:100;\n"
"border-radius:5px\n"
"}\n"
"\n"
"#left_menu_frame QPushButton:hover\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#main_frame\n"
"{\n"
"font-family:rockwell;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_frame = QFrame(self.centralwidget)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu_frame.sizePolicy().hasHeightForWidth())
        self.left_menu_frame.setSizePolicy(sizePolicy)
        self.left_menu_frame.setMinimumSize(QSize(0, 0))
        self.left_menu_frame.setMaximumSize(QSize(0, 16777215))
        self.left_menu_frame.setStyleSheet(u"")
        self.left_menu_frame.setFrameShape(QFrame.Box)
        self.left_menu_frame.setFrameShadow(QFrame.Plain)
        self.left_menu_frame.setLineWidth(2)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.header_frame_menu = QFrame(self.left_menu_frame)
        self.header_frame_menu.setObjectName(u"header_frame_menu")
        self.header_frame_menu.setFrameShape(QFrame.NoFrame)
        self.header_frame_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_frame_menu)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_appostman = QLabel(self.header_frame_menu)
        self.label_appostman.setObjectName(u"label_appostman")
        font = QFont()
        font.setFamily(u"Rockwell Condensed")
        font.setPointSize(20)
        self.label_appostman.setFont(font)
        self.label_appostman.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_appostman)


        self.verticalLayout_2.addWidget(self.header_frame_menu)

        self.main_frame_menu = QFrame(self.left_menu_frame)
        self.main_frame_menu.setObjectName(u"main_frame_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame_menu.sizePolicy().hasHeightForWidth())
        self.main_frame_menu.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Palatino Linotype")
        font1.setPointSize(12)
        self.main_frame_menu.setFont(font1)
        self.main_frame_menu.setFrameShape(QFrame.StyledPanel)
        self.main_frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line_left_footer = QFrame(self.main_frame_menu)
        self.line_left_footer.setObjectName(u"line_left_footer")
        self.line_left_footer.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line_left_footer.setFrameShadow(QFrame.Sunken)
        self.line_left_footer.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line_left_footer)

        self.button_dashboard = QPushButton(self.main_frame_menu)
        self.button_dashboard.setObjectName(u"button_dashboard")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_dashboard.sizePolicy().hasHeightForWidth())
        self.button_dashboard.setSizePolicy(sizePolicy2)
        self.button_dashboard.setMaximumSize(QSize(200, 40))
        self.button_dashboard.setFont(font1)
        self.button_dashboard.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_dashboard.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"resources/main-window-icons/dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_dashboard.setIcon(icon1)
        self.button_dashboard.setIconSize(QSize(27, 27))

        self.verticalLayout_3.addWidget(self.button_dashboard)

        self.button_recipients = QPushButton(self.main_frame_menu)
        self.button_recipients.setObjectName(u"button_recipients")
        self.button_recipients.setMaximumSize(QSize(200, 40))
        self.button_recipients.setFont(font1)
        self.button_recipients.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_recipients.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"resources/main-window-icons/people.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_recipients.setIcon(icon2)
        self.button_recipients.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.button_recipients)

        self.button_messages = QPushButton(self.main_frame_menu)
        self.button_messages.setObjectName(u"button_messages")
        self.button_messages.setMaximumSize(QSize(200, 40))
        self.button_messages.setFont(font1)
        self.button_messages.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_messages.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"resources/main-window-icons/message.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_messages.setIcon(icon3)
        self.button_messages.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.button_messages)

        self.button_configurations = QPushButton(self.main_frame_menu)
        self.button_configurations.setObjectName(u"button_configurations")
        self.button_configurations.setMaximumSize(QSize(200, 40))
        self.button_configurations.setFont(font1)
        self.button_configurations.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_configurations.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"resources/main-window-icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_configurations.setIcon(icon4)
        self.button_configurations.setIconSize(QSize(23, 23))

        self.verticalLayout_3.addWidget(self.button_configurations)

        self.button_help = QPushButton(self.main_frame_menu)
        self.button_help.setObjectName(u"button_help")
        self.button_help.setMaximumSize(QSize(200, 40))
        self.button_help.setFont(font1)
        self.button_help.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_help.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"resources/main-window-icons/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_help.setIcon(icon5)
        self.button_help.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.button_help)

        self.button_about = QPushButton(self.main_frame_menu)
        self.button_about.setObjectName(u"button_about")
        self.button_about.setMaximumSize(QSize(200, 40))
        self.button_about.setFont(font1)
        self.button_about.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_about.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"resources/main-window-icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_about.setIcon(icon6)
        self.button_about.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.button_about)

        self.line_left_header = QFrame(self.main_frame_menu)
        self.line_left_header.setObjectName(u"line_left_header")
        self.line_left_header.setFrameShadow(QFrame.Raised)
        self.line_left_header.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line_left_header)


        self.verticalLayout_2.addWidget(self.main_frame_menu)

        self.footer_frame_menu = QFrame(self.left_menu_frame)
        self.footer_frame_menu.setObjectName(u"footer_frame_menu")
        font2 = QFont()
        font2.setFamily(u"Rockwell")
        self.footer_frame_menu.setFont(font2)
        self.footer_frame_menu.setFrameShape(QFrame.StyledPanel)
        self.footer_frame_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame_menu)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_version = QLabel(self.footer_frame_menu)
        self.label_version.setObjectName(u"label_version")
        font3 = QFont()
        font3.setFamily(u"Rockwell")
        font3.setPointSize(10)
        self.label_version.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_version)


        self.verticalLayout_2.addWidget(self.footer_frame_menu)


        self.horizontalLayout.addWidget(self.left_menu_frame)

        self.central_frame = QFrame(self.centralwidget)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setStyleSheet(u"border-radius: 5px;")
        self.central_frame.setFrameShape(QFrame.NoFrame)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.central_frame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 6, 0)
        self.header_frame = QFrame(self.central_frame)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(200, 208, 213);\n"
"border-radius:5px;")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 10, 0, 0)
        self.button_menu = QPushButton(self.header_left_frame)
        self.button_menu.setObjectName(u"button_menu")
        self.button_menu.setMinimumSize(QSize(35, 35))
        self.button_menu.setMaximumSize(QSize(30, 30))
        self.button_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_menu.setLayoutDirection(Qt.LeftToRight)
        self.button_menu.setStyleSheet(u"#header_frame QPushButton\n"
"{\n"
"opacity: 100;\n"
"border-radius:10px;\n"
"padding-left: 1px;\n"
"}\n"
"\n"
"#header_frame QPushButton:hover\n"
"{\n"
"background-color: rgb(233, 242, 249);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"resources/main-window-icons/left-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_menu.setIcon(icon7)
        self.button_menu.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.button_menu)

        self.label_menu = QLabel(self.header_left_frame)
        self.label_menu.setObjectName(u"label_menu")
        font4 = QFont()
        font4.setFamily(u"Palatino Linotype")
        font4.setPointSize(10)
        self.label_menu.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_menu)


        self.horizontalLayout_2.addWidget(self.header_left_frame, 0, Qt.AlignTop)

        self.header_central_frame = QFrame(self.header_frame)
        self.header_central_frame.setObjectName(u"header_central_frame")
        self.header_central_frame.setFrameShape(QFrame.StyledPanel)
        self.header_central_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.header_central_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(25, 0, 0, 0)
        self.spacer_frame_left = QFrame(self.header_central_frame)
        self.spacer_frame_left.setObjectName(u"spacer_frame_left")
        sizePolicy.setHeightForWidth(self.spacer_frame_left.sizePolicy().hasHeightForWidth())
        self.spacer_frame_left.setSizePolicy(sizePolicy)
        self.spacer_frame_left.setFrameShape(QFrame.StyledPanel)
        self.spacer_frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.spacer_frame_left)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.horizontalLayout_8.addWidget(self.spacer_frame_left)

        self.label_logo = QLabel(self.header_central_frame)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(70, 60))
        self.label_logo.setPixmap(QPixmap(u"resources/mail.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_logo)

        self.spacer_frame_right = QFrame(self.header_central_frame)
        self.spacer_frame_right.setObjectName(u"spacer_frame_right")
        sizePolicy.setHeightForWidth(self.spacer_frame_right.sizePolicy().hasHeightForWidth())
        self.spacer_frame_right.setSizePolicy(sizePolicy)
        self.spacer_frame_right.setFrameShape(QFrame.StyledPanel)
        self.spacer_frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.spacer_frame_right)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)

        self.horizontalLayout_8.addWidget(self.spacer_frame_right)


        self.horizontalLayout_2.addWidget(self.header_central_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.button_minimize = QPushButton(self.header_right_frame)
        self.button_minimize.setObjectName(u"button_minimize")
        self.button_minimize.setMinimumSize(QSize(35, 35))
        self.button_minimize.setMaximumSize(QSize(35, 35))
        self.button_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_minimize.setStyleSheet(u"#header_frame QPushButton\n"
"{\n"
"opacity: 100;\n"
"border-radius:10px\n"
"}\n"
"\n"
"#header_frame QPushButton:hover\n"
"{\n"
"background-color: rgb(233, 242, 249);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"resources/main-window-icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon8)
        self.button_minimize.setIconSize(QSize(21, 18))

        self.horizontalLayout_7.addWidget(self.button_minimize)

        self.button_restore = QPushButton(self.header_right_frame)
        self.button_restore.setObjectName(u"button_restore")
        self.button_restore.setMinimumSize(QSize(35, 35))
        self.button_restore.setMaximumSize(QSize(35, 35))
        self.button_restore.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_restore.setStyleSheet(u"#header_frame QPushButton\n"
"{\n"
"opacity: 100;\n"
"border-radius:10px\n"
"}\n"
"\n"
"#header_frame QPushButton:hover\n"
"{\n"
"background-color: rgb(233, 242, 249);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"resources/main-window-icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_restore.setIcon(icon9)
        self.button_restore.setIconSize(QSize(18, 18))

        self.horizontalLayout_7.addWidget(self.button_restore, 0, Qt.AlignRight)

        self.button_close = QPushButton(self.header_right_frame)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setMinimumSize(QSize(35, 35))
        self.button_close.setMaximumSize(QSize(35, 35))
        self.button_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_close.setStyleSheet(u"#header_frame QPushButton\n"
"{\n"
"opacity: 100;\n"
"border-radius:10px\n"
"}\n"
"\n"
"#header_frame QPushButton:hover\n"
"{\n"
"background-color: rgb(233, 242, 249);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"resources/main-window-icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon10)
        self.button_close.setIconSize(QSize(18, 18))

        self.horizontalLayout_7.addWidget(self.button_close, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.header_right_frame, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_frame = QFrame(self.central_frame)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy3)
        self.main_frame.setStyleSheet(u"background-color: rgb(200, 208, 213);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.pages = QStackedWidget(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.pages.setFont(font1)
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.verticalLayout_7 = QVBoxLayout(self.dashboard)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_title_1 = QFrame(self.dashboard)
        self.frame_title_1.setObjectName(u"frame_title_1")
        self.frame_title_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_title_1 = QLabel(self.frame_title_1)
        self.label_title_1.setObjectName(u"label_title_1")
        font5 = QFont()
        font5.setFamily(u"Rockwell")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_title_1.setFont(font5)
        self.label_title_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_title_1, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.frame_title_1, 0, Qt.AlignTop)

        self.frame_main_page1 = QFrame(self.dashboard)
        self.frame_main_page1.setObjectName(u"frame_main_page1")
        sizePolicy1.setHeightForWidth(self.frame_main_page1.sizePolicy().hasHeightForWidth())
        self.frame_main_page1.setSizePolicy(sizePolicy1)
        self.frame_main_page1.setFrameShape(QFrame.StyledPanel)
        self.frame_main_page1.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_main_page1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.frame_main_page1)

        self.pages.addWidget(self.dashboard)
        self.recipients = QWidget()
        self.recipients.setObjectName(u"recipients")
        self.verticalLayout_10 = QVBoxLayout(self.recipients)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_title_2 = QFrame(self.recipients)
        self.frame_title_2.setObjectName(u"frame_title_2")
        self.frame_title_2.setFont(font2)
        self.frame_title_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_title_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_title_2 = QLabel(self.frame_title_2)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setFont(font5)
        self.label_title_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_title_2, 0, Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_title_2)

        self.frame_main_page2 = QFrame(self.recipients)
        self.frame_main_page2.setObjectName(u"frame_main_page2")
        sizePolicy1.setHeightForWidth(self.frame_main_page2.sizePolicy().hasHeightForWidth())
        self.frame_main_page2.setSizePolicy(sizePolicy1)
        self.frame_main_page2.setFrameShape(QFrame.StyledPanel)
        self.frame_main_page2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_main_page2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.frame_destinatarios_encontrados = QFrame(self.frame_main_page2)
        self.frame_destinatarios_encontrados.setObjectName(u"frame_destinatarios_encontrados")
        self.frame_destinatarios_encontrados.setStyleSheet(u"background-color: rgb(217, 225, 230);")
        self.frame_destinatarios_encontrados.setFrameShape(QFrame.StyledPanel)
        self.frame_destinatarios_encontrados.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_destinatarios_encontrados)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_destinatarios_encontrados)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 374, 317))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setFamily(u"Palatino Linotype")
        font6.setBold(True)
        font6.setWeight(75)
        self.label.setFont(font6)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 140))
        font7 = QFont()
        font7.setFamily(u"Palatino Linotype")
        self.label_2.setFont(font7)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_2)

        self.button_search_recipients = QPushButton(self.scrollAreaWidgetContents)
        self.button_search_recipients.setObjectName(u"button_search_recipients")
        sizePolicy2.setHeightForWidth(self.button_search_recipients.sizePolicy().hasHeightForWidth())
        self.button_search_recipients.setSizePolicy(sizePolicy2)
        self.button_search_recipients.setMinimumSize(QSize(120, 40))
        self.button_search_recipients.setFont(font1)
        self.button_search_recipients.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_search_recipients.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(158, 195, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.verticalLayout_20.addWidget(self.button_search_recipients, 0, Qt.AlignHCenter)

        self.label_file_path_recipients = QLabel(self.scrollAreaWidgetContents)
        self.label_file_path_recipients.setObjectName(u"label_file_path_recipients")
        self.label_file_path_recipients.setMaximumSize(QSize(16777215, 60))
        font8 = QFont()
        font8.setFamily(u"Rockwell")
        font8.setPointSize(12)
        self.label_file_path_recipients.setFont(font8)
        self.label_file_path_recipients.setAlignment(Qt.AlignCenter)
        self.label_file_path_recipients.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_file_path_recipients)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 70))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.spacer_frame_3 = QFrame(self.frame_3)
        self.spacer_frame_3.setObjectName(u"spacer_frame_3")
        self.spacer_frame_3.setFrameShape(QFrame.StyledPanel)
        self.spacer_frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.spacer_frame_3)

        self.button_validar = QPushButton(self.frame_3)
        self.button_validar.setObjectName(u"button_validar")
        self.button_validar.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.button_validar.sizePolicy().hasHeightForWidth())
        self.button_validar.setSizePolicy(sizePolicy2)
        self.button_validar.setMinimumSize(QSize(150, 40))
        self.button_validar.setFont(font1)
        self.button_validar.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_validar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 208, 213);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.button_validar)

        self.button_cadastrar = QPushButton(self.frame_3)
        self.button_cadastrar.setObjectName(u"button_cadastrar")
        self.button_cadastrar.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.button_cadastrar.sizePolicy().hasHeightForWidth())
        self.button_cadastrar.setSizePolicy(sizePolicy2)
        self.button_cadastrar.setMinimumSize(QSize(150, 40))
        self.button_cadastrar.setFont(font1)
        self.button_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_cadastrar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 208, 213);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.button_cadastrar)

        self.spacer_frame_4 = QFrame(self.frame_3)
        self.spacer_frame_4.setObjectName(u"spacer_frame_4")
        self.spacer_frame_4.setFrameShape(QFrame.StyledPanel)
        self.spacer_frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.spacer_frame_4)


        self.verticalLayout_20.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_10.addWidget(self.scrollArea)


        self.horizontalLayout_9.addWidget(self.frame_destinatarios_encontrados)

        self.frame_2 = QFrame(self.frame_main_page2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(217, 225, 230);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.scrollArea_2 = QScrollArea(self.frame_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 279, 143))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_recipients = QLabel(self.scrollAreaWidgetContents_2)
        self.label_recipients.setObjectName(u"label_recipients")
        self.label_recipients.setMinimumSize(QSize(0, 50))
        font9 = QFont()
        font9.setFamily(u"Palatino Linotype")
        font9.setPointSize(16)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_recipients.setFont(font9)
        self.label_recipients.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_recipients)

        self.table_recipients = QTableWidget(self.scrollAreaWidgetContents_2)
        if (self.table_recipients.columnCount() < 2):
            self.table_recipients.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_recipients.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_recipients.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_recipients.setObjectName(u"table_recipients")
        self.table_recipients.setFont(font1)
        self.table_recipients.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.table_recipients.setStyleSheet(u"background-color: rgb(232, 240, 244);\n"
"")
        self.table_recipients.setFrameShape(QFrame.NoFrame)
        self.table_recipients.setAlternatingRowColors(True)
        self.table_recipients.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_recipients.setShowGrid(True)
        self.table_recipients.setGridStyle(Qt.SolidLine)
        self.table_recipients.setWordWrap(False)
        self.table_recipients.setCornerButtonEnabled(False)

        self.verticalLayout_21.addWidget(self.table_recipients)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_11.addWidget(self.scrollArea_2)


        self.horizontalLayout_9.addWidget(self.frame_2)


        self.verticalLayout_10.addWidget(self.frame_main_page2)

        self.pages.addWidget(self.recipients)
        self.messages = QWidget()
        self.messages.setObjectName(u"messages")
        self.verticalLayout_12 = QVBoxLayout(self.messages)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_title_3 = QFrame(self.messages)
        self.frame_title_3.setObjectName(u"frame_title_3")
        self.frame_title_3.setFont(font8)
        self.frame_title_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_title_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_title_3 = QLabel(self.frame_title_3)
        self.label_title_3.setObjectName(u"label_title_3")
        self.label_title_3.setFont(font5)
        self.label_title_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_title_3, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_title_3)

        self.frame_main_page3 = QFrame(self.messages)
        self.frame_main_page3.setObjectName(u"frame_main_page3")
        sizePolicy1.setHeightForWidth(self.frame_main_page3.sizePolicy().hasHeightForWidth())
        self.frame_main_page3.setSizePolicy(sizePolicy1)
        self.frame_main_page3.setFrameShape(QFrame.StyledPanel)
        self.frame_main_page3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_main_page3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, 0, -1)
        self.frame_cadastrar_mensagens = QFrame(self.frame_main_page3)
        self.frame_cadastrar_mensagens.setObjectName(u"frame_cadastrar_mensagens")
        self.frame_cadastrar_mensagens.setStyleSheet(u"background-color: rgb(217, 225, 230);")
        self.frame_cadastrar_mensagens.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastrar_mensagens.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_cadastrar_mensagens)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.frame_cadastrar_mensagens)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        sizePolicy.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy)
        self.scrollArea_5.setStyleSheet(u"")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 374, 353))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(9, 9, 9, 9)
        self.label_5 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setFont(font6)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_5)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 140))
        self.label_6.setFont(font7)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_6.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.label_6)

        self.button_search_message = QPushButton(self.scrollAreaWidgetContents_7)
        self.button_search_message.setObjectName(u"button_search_message")
        sizePolicy2.setHeightForWidth(self.button_search_message.sizePolicy().hasHeightForWidth())
        self.button_search_message.setSizePolicy(sizePolicy2)
        self.button_search_message.setMinimumSize(QSize(120, 40))
        self.button_search_message.setFont(font1)
        self.button_search_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_search_message.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(158, 195, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.verticalLayout_24.addWidget(self.button_search_message, 0, Qt.AlignHCenter)

        self.label_file_path_message = QLabel(self.scrollAreaWidgetContents_7)
        self.label_file_path_message.setObjectName(u"label_file_path_message")
        self.label_file_path_message.setMaximumSize(QSize(16777215, 60))
        self.label_file_path_message.setFont(font8)
        self.label_file_path_message.setAlignment(Qt.AlignCenter)
        self.label_file_path_message.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.label_file_path_message)

        self.lineEdit_message_name = QLineEdit(self.scrollAreaWidgetContents_7)
        self.lineEdit_message_name.setObjectName(u"lineEdit_message_name")
        self.lineEdit_message_name.setEnabled(False)
        self.lineEdit_message_name.setMinimumSize(QSize(250, 30))
        self.lineEdit_message_name.setMaximumSize(QSize(250, 30))
        font10 = QFont()
        font10.setFamily(u"Palatino Linotype")
        font10.setPointSize(12)
        font10.setItalic(False)
        self.lineEdit_message_name.setFont(font10)
        self.lineEdit_message_name.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(200, 208, 213);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(236, 244, 248);\n"
"}")
        self.lineEdit_message_name.setFrame(False)
        self.lineEdit_message_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.lineEdit_message_name, 0, Qt.AlignHCenter)

        self.frame_botoes_message = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_botoes_message.setObjectName(u"frame_botoes_message")
        self.frame_botoes_message.setMaximumSize(QSize(16777215, 70))
        self.frame_botoes_message.setStyleSheet(u"")
        self.frame_botoes_message.setFrameShape(QFrame.StyledPanel)
        self.frame_botoes_message.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_botoes_message)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.spacer_frame_7 = QFrame(self.frame_botoes_message)
        self.spacer_frame_7.setObjectName(u"spacer_frame_7")
        self.spacer_frame_7.setFrameShape(QFrame.StyledPanel)
        self.spacer_frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.spacer_frame_7)

        self.button_validar_message = QPushButton(self.frame_botoes_message)
        self.button_validar_message.setObjectName(u"button_validar_message")
        self.button_validar_message.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.button_validar_message.sizePolicy().hasHeightForWidth())
        self.button_validar_message.setSizePolicy(sizePolicy2)
        self.button_validar_message.setMinimumSize(QSize(150, 40))
        self.button_validar_message.setFont(font1)
        self.button_validar_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_validar_message.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 208, 213);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.button_validar_message)

        self.button_cadastrar_message = QPushButton(self.frame_botoes_message)
        self.button_cadastrar_message.setObjectName(u"button_cadastrar_message")
        self.button_cadastrar_message.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.button_cadastrar_message.sizePolicy().hasHeightForWidth())
        self.button_cadastrar_message.setSizePolicy(sizePolicy2)
        self.button_cadastrar_message.setMinimumSize(QSize(150, 40))
        self.button_cadastrar_message.setFont(font1)
        self.button_cadastrar_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_cadastrar_message.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(200, 208, 213);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.button_cadastrar_message)

        self.spacer_frame_8 = QFrame(self.frame_botoes_message)
        self.spacer_frame_8.setObjectName(u"spacer_frame_8")
        self.spacer_frame_8.setFrameShape(QFrame.StyledPanel)
        self.spacer_frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.spacer_frame_8)


        self.verticalLayout_24.addWidget(self.frame_botoes_message)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)

        self.horizontalLayout_14.addWidget(self.scrollArea_5)


        self.horizontalLayout_13.addWidget(self.frame_cadastrar_mensagens)

        self.frame_mensagens_cadastradas = QFrame(self.frame_main_page3)
        self.frame_mensagens_cadastradas.setObjectName(u"frame_mensagens_cadastradas")
        self.frame_mensagens_cadastradas.setStyleSheet(u"background-color: rgb(217, 225, 230);")
        self.frame_mensagens_cadastradas.setFrameShape(QFrame.StyledPanel)
        self.frame_mensagens_cadastradas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_mensagens_cadastradas)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, 0, -1)
        self.scrollArea_6 = QScrollArea(self.frame_mensagens_cadastradas)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 253, 189))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_recipients_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_recipients_2.setObjectName(u"label_recipients_2")
        self.label_recipients_2.setMinimumSize(QSize(0, 50))
        self.label_recipients_2.setFont(font9)
        self.label_recipients_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_recipients_2)

        self.listWidget_message = QListWidget(self.scrollAreaWidgetContents_6)
        self.listWidget_message.setObjectName(u"listWidget_message")
        self.listWidget_message.setFont(font1)
        self.listWidget_message.setStyleSheet(u"background-color: rgb(232, 240, 244);")

        self.verticalLayout_23.addWidget(self.listWidget_message)

        self.button_excluir_message = QPushButton(self.scrollAreaWidgetContents_6)
        self.button_excluir_message.setObjectName(u"button_excluir_message")
        sizePolicy2.setHeightForWidth(self.button_excluir_message.sizePolicy().hasHeightForWidth())
        self.button_excluir_message.setSizePolicy(sizePolicy2)
        self.button_excluir_message.setMinimumSize(QSize(120, 40))
        self.button_excluir_message.setFont(font1)
        self.button_excluir_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_excluir_message.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 75, 78);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.verticalLayout_23.addWidget(self.button_excluir_message, 0, Qt.AlignHCenter)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_15.addWidget(self.scrollArea_6)


        self.horizontalLayout_13.addWidget(self.frame_mensagens_cadastradas)


        self.verticalLayout_12.addWidget(self.frame_main_page3)

        self.pages.addWidget(self.messages)
        self.configurations = QWidget()
        self.configurations.setObjectName(u"configurations")
        self.verticalLayout_14 = QVBoxLayout(self.configurations)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.frame_title_4 = QFrame(self.configurations)
        self.frame_title_4.setObjectName(u"frame_title_4")
        self.frame_title_4.setFont(font2)
        self.frame_title_4.setFrameShape(QFrame.StyledPanel)
        self.frame_title_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_title_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_title_4 = QLabel(self.frame_title_4)
        self.label_title_4.setObjectName(u"label_title_4")
        self.label_title_4.setFont(font5)
        self.label_title_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_title_4, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.frame_title_4)

        self.frame_main_page4 = QFrame(self.configurations)
        self.frame_main_page4.setObjectName(u"frame_main_page4")
        sizePolicy1.setHeightForWidth(self.frame_main_page4.sizePolicy().hasHeightForWidth())
        self.frame_main_page4.setSizePolicy(sizePolicy1)
        self.frame_main_page4.setStyleSheet(u"")
        self.frame_main_page4.setFrameShape(QFrame.StyledPanel)
        self.frame_main_page4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_main_page4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.frame = QFrame(self.frame_main_page4)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(217, 225, 230);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(20, 0, 20, 0)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u".QTabWidget::pane{\n"
"    border:none\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	background-color: rgb(240, 240, 240);\n"
"	font-family: 'Rockwell';\n"
"    font-size: 14px; /* Tamanho da fonte */\n"
"    min-width: 80px; /* Largura m\u00ednima dos bot\u00f5es das abas */\n"
"    padding: 8px; /* Espa\u00e7amento interno */\n"
"    border: 0.5px solid  rgb(232, 232, 232); \n"
"}\n"
"\n"
"QTabBar::tab::selected {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.tab_smtp = QWidget()
        self.tab_smtp.setObjectName(u"tab_smtp")
        self.verticalLayout_22 = QVBoxLayout(self.tab_smtp)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, 0, 9, 0)
        self.label_7 = QLabel(self.tab_smtp)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 50))
        self.label_7.setFont(font6)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_7)

        self.label_8 = QLabel(self.tab_smtp)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 140))
        self.label_8.setFont(font7)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_8.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label_8)

        self.frame_4 = QFrame(self.tab_smtp)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer)

        self.lineEdit_smtp_servidor = QLineEdit(self.frame_4)
        self.lineEdit_smtp_servidor.setObjectName(u"lineEdit_smtp_servidor")
        self.lineEdit_smtp_servidor.setEnabled(True)
        self.lineEdit_smtp_servidor.setMinimumSize(QSize(250, 30))
        self.lineEdit_smtp_servidor.setMaximumSize(QSize(250, 30))
        self.lineEdit_smtp_servidor.setFont(font10)
        self.lineEdit_smtp_servidor.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(236, 244, 248);\n"
"}")
        self.lineEdit_smtp_servidor.setFrame(False)
        self.lineEdit_smtp_servidor.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.lineEdit_smtp_servidor, 0, Qt.AlignBottom)

        self.lineEdit_smtp_porta = QLineEdit(self.frame_4)
        self.lineEdit_smtp_porta.setObjectName(u"lineEdit_smtp_porta")
        self.lineEdit_smtp_porta.setEnabled(True)
        self.lineEdit_smtp_porta.setMinimumSize(QSize(250, 30))
        self.lineEdit_smtp_porta.setMaximumSize(QSize(250, 30))
        self.lineEdit_smtp_porta.setFont(font10)
        self.lineEdit_smtp_porta.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(236, 244, 248);\n"
"}")
        self.lineEdit_smtp_porta.setFrame(False)
        self.lineEdit_smtp_porta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.lineEdit_smtp_porta, 0, Qt.AlignBottom)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)


        self.verticalLayout_22.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.tab_smtp)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_19.setSpacing(20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)

        self.lineEdit_smtp_email = QLineEdit(self.frame_5)
        self.lineEdit_smtp_email.setObjectName(u"lineEdit_smtp_email")
        self.lineEdit_smtp_email.setEnabled(True)
        self.lineEdit_smtp_email.setMinimumSize(QSize(250, 30))
        self.lineEdit_smtp_email.setMaximumSize(QSize(250, 30))
        self.lineEdit_smtp_email.setFont(font10)
        self.lineEdit_smtp_email.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(236, 244, 248);\n"
"}")
        self.lineEdit_smtp_email.setFrame(False)
        self.lineEdit_smtp_email.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.lineEdit_smtp_email, 0, Qt.AlignTop)

        self.lineEdit_smtp_senha = QLineEdit(self.frame_5)
        self.lineEdit_smtp_senha.setObjectName(u"lineEdit_smtp_senha")
        self.lineEdit_smtp_senha.setEnabled(True)
        self.lineEdit_smtp_senha.setMinimumSize(QSize(250, 30))
        self.lineEdit_smtp_senha.setMaximumSize(QSize(250, 30))
        self.lineEdit_smtp_senha.setFont(font10)
        self.lineEdit_smtp_senha.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(236, 244, 248);\n"
"}")
        self.lineEdit_smtp_senha.setFrame(False)
        self.lineEdit_smtp_senha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.lineEdit_smtp_senha, 0, Qt.AlignTop)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)


        self.verticalLayout_22.addWidget(self.frame_5)

        self.button_smtp_validate = QPushButton(self.tab_smtp)
        self.button_smtp_validate.setObjectName(u"button_smtp_validate")
        sizePolicy2.setHeightForWidth(self.button_smtp_validate.sizePolicy().hasHeightForWidth())
        self.button_smtp_validate.setSizePolicy(sizePolicy2)
        self.button_smtp_validate.setMinimumSize(QSize(120, 40))
        self.button_smtp_validate.setFont(font1)
        self.button_smtp_validate.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_smtp_validate.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(158, 195, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.verticalLayout_22.addWidget(self.button_smtp_validate, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab_smtp, "")
        self.tab_imap = QWidget()
        self.tab_imap.setObjectName(u"tab_imap")
        self.verticalLayout_25 = QVBoxLayout(self.tab_imap)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(9, 0, 9, 0)
        self.label_9 = QLabel(self.tab_imap)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 50))
        self.label_9.setFont(font6)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_9)

        self.label_10 = QLabel(self.tab_imap)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 140))
        self.label_10.setFont(font7)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_10.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.label_10)

        self.frame_6 = QFrame(self.tab_imap)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_20.setSpacing(20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_5)

        self.lineEdit_imap_servidor = QLineEdit(self.frame_6)
        self.lineEdit_imap_servidor.setObjectName(u"lineEdit_imap_servidor")
        self.lineEdit_imap_servidor.setEnabled(True)
        self.lineEdit_imap_servidor.setMinimumSize(QSize(250, 30))
        self.lineEdit_imap_servidor.setMaximumSize(QSize(250, 30))
        self.lineEdit_imap_servidor.setFont(font10)
        self.lineEdit_imap_servidor.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(236, 244, 248);\n"
"}")
        self.lineEdit_imap_servidor.setFrame(False)
        self.lineEdit_imap_servidor.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lineEdit_imap_servidor, 0, Qt.AlignBottom)

        self.lineEdit_imap_porta = QLineEdit(self.frame_6)
        self.lineEdit_imap_porta.setObjectName(u"lineEdit_imap_porta")
        self.lineEdit_imap_porta.setEnabled(True)
        self.lineEdit_imap_porta.setMinimumSize(QSize(250, 30))
        self.lineEdit_imap_porta.setMaximumSize(QSize(250, 30))
        self.lineEdit_imap_porta.setFont(font10)
        self.lineEdit_imap_porta.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(236, 244, 248);\n"
"}")
        self.lineEdit_imap_porta.setFrame(False)
        self.lineEdit_imap_porta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lineEdit_imap_porta, 0, Qt.AlignBottom)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)


        self.verticalLayout_25.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.tab_imap)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)

        self.lineEdit_imap_email = QLineEdit(self.frame_7)
        self.lineEdit_imap_email.setObjectName(u"lineEdit_imap_email")
        self.lineEdit_imap_email.setEnabled(True)
        self.lineEdit_imap_email.setMinimumSize(QSize(250, 30))
        self.lineEdit_imap_email.setMaximumSize(QSize(250, 30))
        self.lineEdit_imap_email.setFont(font10)
        self.lineEdit_imap_email.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(236, 244, 248);\n"
"}")
        self.lineEdit_imap_email.setFrame(False)
        self.lineEdit_imap_email.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lineEdit_imap_email, 0, Qt.AlignTop)

        self.lineEdit_smtp_senha_2 = QLineEdit(self.frame_7)
        self.lineEdit_smtp_senha_2.setObjectName(u"lineEdit_smtp_senha_2")
        self.lineEdit_smtp_senha_2.setEnabled(True)
        self.lineEdit_smtp_senha_2.setMinimumSize(QSize(250, 30))
        self.lineEdit_smtp_senha_2.setMaximumSize(QSize(250, 30))
        self.lineEdit_smtp_senha_2.setFont(font10)
        self.lineEdit_smtp_senha_2.setStyleSheet(u"QLineEdit\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(236, 244, 248);\n"
"}")
        self.lineEdit_smtp_senha_2.setFrame(False)
        self.lineEdit_smtp_senha_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lineEdit_smtp_senha_2, 0, Qt.AlignTop)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)


        self.verticalLayout_25.addWidget(self.frame_7)

        self.button_imap_validate = QPushButton(self.tab_imap)
        self.button_imap_validate.setObjectName(u"button_imap_validate")
        sizePolicy2.setHeightForWidth(self.button_imap_validate.sizePolicy().hasHeightForWidth())
        self.button_imap_validate.setSizePolicy(sizePolicy2)
        self.button_imap_validate.setMinimumSize(QSize(120, 40))
        self.button_imap_validate.setFont(font1)
        self.button_imap_validate.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_imap_validate.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(158, 195, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.button_imap_validate, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab_imap, "")
        self.tab_envios = QWidget()
        self.tab_envios.setObjectName(u"tab_envios")
        self.horizontalLayout_22 = QHBoxLayout(self.tab_envios)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(9, 0, -1, 9)
        self.scrollArea_3 = QScrollArea(self.tab_envios)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 468, 424))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 50))
        self.label_11.setFont(font6)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_11)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_11)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"#frame_12 {\n"
"background-color: rgb(232, 240, 244);\n"
"border-radius: 5px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_12)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(9, -1, -1, -1)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setStyleSheet(u"background-color: rgb(217, 225, 230);")
        self.frame_13.setFrameShape(QFrame.Box)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(50, -1, 50, -1)
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(200, 16777215))
        self.label_12.setFont(font7)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_12.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.label_12, 0, Qt.AlignVCenter)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_10)

        self.comboBox_dia = QComboBox(self.frame_13)
        self.comboBox_dia.addItem("")
        self.comboBox_dia.addItem("")
        self.comboBox_dia.addItem("")
        self.comboBox_dia.addItem("")
        self.comboBox_dia.addItem("")
        self.comboBox_dia.addItem("")
        self.comboBox_dia.addItem("")
        self.comboBox_dia.setObjectName(u"comboBox_dia")
        self.comboBox_dia.setMinimumSize(QSize(135, 0))
        font11 = QFont()
        self.comboBox_dia.setFont(font11)
        self.comboBox_dia.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_dia.setStyleSheet(u"QComboBox {\n"
"    border-radius: 5px;\n"
"    padding: 2px 20px 2px 10px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: #333333;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.comboBox_dia.setFrame(True)

        self.horizontalLayout_23.addWidget(self.comboBox_dia, 0, Qt.AlignLeft)


        self.verticalLayout_32.addWidget(self.frame_13)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setStyleSheet(u"background-color: rgb(217, 225, 230);")
        self.frame_16.setFrameShape(QFrame.Box)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(50, -1, 50, -1)
        self.label_13 = QLabel(self.frame_16)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(50, 0))
        self.label_13.setMaximumSize(QSize(80, 16777215))
        self.label_13.setFont(font7)
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_13.setWordWrap(True)

        self.horizontalLayout_24.addWidget(self.label_13)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_11)

        self.timeEdit_horario = QTimeEdit(self.frame_16)
        self.timeEdit_horario.setObjectName(u"timeEdit_horario")
        self.timeEdit_horario.setFont(font11)
        self.timeEdit_horario.setCursor(QCursor(Qt.PointingHandCursor))
        self.timeEdit_horario.setStyleSheet(u"QTimeEdit {\n"
"    border-radius: 5px;\n"
"    padding: 2px 10px;\n"
"    background-color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: #333333;\n"
"}\n"
"\n"
"QTimeEdit::up-button, QTimeEdit::down-button {\n"
"    width: 20px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_24.addWidget(self.timeEdit_horario, 0, Qt.AlignLeft)


        self.verticalLayout_32.addWidget(self.frame_16)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 50))
        self.frame_14.setStyleSheet(u"background-color: rgb(217, 225, 230);")
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(50, -1, 50, -1)
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(200, 16777215))
        self.label_14.setFont(font7)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_14.setWordWrap(True)

        self.horizontalLayout_25.addWidget(self.label_14, 0, Qt.AlignVCenter)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_12)

        self.comboBox_genero = QComboBox(self.frame_14)
        self.comboBox_genero.addItem("")
        self.comboBox_genero.addItem("")
        self.comboBox_genero.addItem("")
        self.comboBox_genero.setObjectName(u"comboBox_genero")
        self.comboBox_genero.setFont(font11)
        self.comboBox_genero.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_genero.setStyleSheet(u"QComboBox {\n"
"    border-radius: 5px;\n"
"    padding: 2px 20px 2px 10px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: #333333;\n"
"    font-size: 14px;\n"
"}\n"
"")

        self.horizontalLayout_25.addWidget(self.comboBox_genero, 0, Qt.AlignLeft)


        self.verticalLayout_32.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setStyleSheet(u"background-color: rgb(217, 225, 230);")
        self.frame_15.setFrameShape(QFrame.Box)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(50, -1, 50, -1)
        self.checkBox_idade = QCheckBox(self.frame_15)
        self.checkBox_idade.setObjectName(u"checkBox_idade")
        self.checkBox_idade.setFont(font1)
        self.checkBox_idade.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_26.addWidget(self.checkBox_idade)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_9)

        self.spinBox_idadeInicial = QSpinBox(self.frame_15)
        self.spinBox_idadeInicial.setObjectName(u"spinBox_idadeInicial")
        self.spinBox_idadeInicial.setEnabled(False)
        self.spinBox_idadeInicial.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_idadeInicial.setStyleSheet(u"QSpinBox {\n"
"    border-radius: 5px;\n"
"    padding: 2px 10px;\n"
"    background-color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: #333333;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    width: 20px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_26.addWidget(self.spinBox_idadeInicial, 0, Qt.AlignLeft)

        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setEnabled(False)
        self.label_16.setMinimumSize(QSize(35, 0))
        self.label_16.setFont(font7)
        self.label_16.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_16.setWordWrap(True)

        self.horizontalLayout_26.addWidget(self.label_16, 0, Qt.AlignVCenter)

        self.spinBox_idadeFinal = QSpinBox(self.frame_15)
        self.spinBox_idadeFinal.setObjectName(u"spinBox_idadeFinal")
        self.spinBox_idadeFinal.setEnabled(False)
        self.spinBox_idadeFinal.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_idadeFinal.setStyleSheet(u"QSpinBox {\n"
"    border-radius: 5px;\n"
"    padding: 2px 10px;\n"
"    background-color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    selection-background-color: #EDEDED;\n"
"    selection-color: #333333;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    width: 20px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_26.addWidget(self.spinBox_idadeFinal, 0, Qt.AlignLeft)


        self.verticalLayout_32.addWidget(self.frame_15)

        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setStyleSheet(u"background-color: rgb(217, 225, 230);")
        self.frame_17.setFrameShape(QFrame.Box)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(50, -1, 50, -1)
        self.checkBox_pais = QCheckBox(self.frame_17)
        self.checkBox_pais.setObjectName(u"checkBox_pais")
        self.checkBox_pais.setFont(font1)
        self.checkBox_pais.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_27.addWidget(self.checkBox_pais)

        self.lineEdit_codigoPais = QLineEdit(self.frame_17)
        self.lineEdit_codigoPais.setObjectName(u"lineEdit_codigoPais")
        self.lineEdit_codigoPais.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.lineEdit_codigoPais.sizePolicy().hasHeightForWidth())
        self.lineEdit_codigoPais.setSizePolicy(sizePolicy2)
        self.lineEdit_codigoPais.setMinimumSize(QSize(100, 25))
        self.lineEdit_codigoPais.setFont(font4)
        self.lineEdit_codigoPais.setStyleSheet(u"background-color: rgb(254, 254, 254);")
        self.lineEdit_codigoPais.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.lineEdit_codigoPais)


        self.verticalLayout_32.addWidget(self.frame_17)

        self.button_imap_validate_2 = QPushButton(self.frame_12)
        self.button_imap_validate_2.setObjectName(u"button_imap_validate_2")
        sizePolicy2.setHeightForWidth(self.button_imap_validate_2.sizePolicy().hasHeightForWidth())
        self.button_imap_validate_2.setSizePolicy(sizePolicy2)
        self.button_imap_validate_2.setMinimumSize(QSize(120, 40))
        self.button_imap_validate_2.setFont(font1)
        self.button_imap_validate_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_imap_validate_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(158, 195, 255);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.verticalLayout_32.addWidget(self.button_imap_validate_2, 0, Qt.AlignHCenter)


        self.verticalLayout_31.addWidget(self.frame_12)


        self.verticalLayout_30.addWidget(self.frame_11)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_22.addWidget(self.scrollArea_3)

        self.scrollArea_7 = QScrollArea(self.tab_envios)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setFrameShadow(QFrame.Raised)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 465, 424))
        self.verticalLayout_29 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_recipients_6 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_recipients_6.setObjectName(u"label_recipients_6")
        self.label_recipients_6.setMinimumSize(QSize(0, 50))
        self.label_recipients_6.setFont(font9)
        self.label_recipients_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_recipients_6)

        self.listWidget_message_5 = QListWidget(self.scrollAreaWidgetContents_11)
        self.listWidget_message_5.setObjectName(u"listWidget_message_5")
        self.listWidget_message_5.setFont(font1)
        self.listWidget_message_5.setStyleSheet(u"background-color: rgb(232, 240, 244);")

        self.verticalLayout_29.addWidget(self.listWidget_message_5)

        self.button_excluir_message_5 = QPushButton(self.scrollAreaWidgetContents_11)
        self.button_excluir_message_5.setObjectName(u"button_excluir_message_5")
        sizePolicy2.setHeightForWidth(self.button_excluir_message_5.sizePolicy().hasHeightForWidth())
        self.button_excluir_message_5.setSizePolicy(sizePolicy2)
        self.button_excluir_message_5.setMinimumSize(QSize(120, 40))
        self.button_excluir_message_5.setFont(font1)
        self.button_excluir_message_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_excluir_message_5.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 75, 78);\n"
"border: 1px solid;\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(212, 220, 226);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.verticalLayout_29.addWidget(self.button_excluir_message_5, 0, Qt.AlignHCenter)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_11)

        self.horizontalLayout_22.addWidget(self.scrollArea_7)

        self.tabWidget.addTab(self.tab_envios, "")

        self.horizontalLayout_16.addWidget(self.tabWidget)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_main_page4)

        self.pages.addWidget(self.configurations)
        self.help = QWidget()
        self.help.setObjectName(u"help")
        self.verticalLayout_16 = QVBoxLayout(self.help)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_title_5 = QFrame(self.help)
        self.frame_title_5.setObjectName(u"frame_title_5")
        self.frame_title_5.setFont(font2)
        self.frame_title_5.setFrameShape(QFrame.StyledPanel)
        self.frame_title_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_title_5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_title_5 = QLabel(self.frame_title_5)
        self.label_title_5.setObjectName(u"label_title_5")
        self.label_title_5.setFont(font5)
        self.label_title_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_title_5, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_title_5)

        self.frame_main_page5 = QFrame(self.help)
        self.frame_main_page5.setObjectName(u"frame_main_page5")
        sizePolicy1.setHeightForWidth(self.frame_main_page5.sizePolicy().hasHeightForWidth())
        self.frame_main_page5.setSizePolicy(sizePolicy1)
        self.frame_main_page5.setFrameShape(QFrame.StyledPanel)
        self.frame_main_page5.setFrameShadow(QFrame.Raised)
        self.frame_main_page5.setLineWidth(1)
        self.gridLayout_5 = QGridLayout(self.frame_main_page5)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_16.addWidget(self.frame_main_page5)

        self.pages.addWidget(self.help)
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.verticalLayout_18 = QVBoxLayout(self.about)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_title_6 = QFrame(self.about)
        self.frame_title_6.setObjectName(u"frame_title_6")
        self.frame_title_6.setFont(font2)
        self.frame_title_6.setFrameShape(QFrame.StyledPanel)
        self.frame_title_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_title_6)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_title_6 = QLabel(self.frame_title_6)
        self.label_title_6.setObjectName(u"label_title_6")
        self.label_title_6.setFont(font5)
        self.label_title_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_title_6, 0, Qt.AlignTop)


        self.verticalLayout_18.addWidget(self.frame_title_6)

        self.frame_main_page6 = QFrame(self.about)
        self.frame_main_page6.setObjectName(u"frame_main_page6")
        sizePolicy1.setHeightForWidth(self.frame_main_page6.sizePolicy().hasHeightForWidth())
        self.frame_main_page6.setSizePolicy(sizePolicy1)
        self.frame_main_page6.setFrameShape(QFrame.StyledPanel)
        self.frame_main_page6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_main_page6)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_18.addWidget(self.frame_main_page6)

        self.pages.addWidget(self.about)

        self.verticalLayout_4.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.central_frame)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMaximumSize(QSize(16777215, 45))
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.frame_8 = QFrame(self.footer_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_copyright = QLabel(self.frame_8)
        self.label_copyright.setObjectName(u"label_copyright")
        self.label_copyright.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_copyright)


        self.horizontalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.footer_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(80, 50, 120, 80))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.central_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_appostman.setText(QCoreApplication.translate("MainWindow", u"APPOSTMAN", None))
        self.button_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.button_recipients.setText(QCoreApplication.translate("MainWindow", u"Destinat\u00e1rios", None))
        self.button_messages.setText(QCoreApplication.translate("MainWindow", u"Mensagens", None))
        self.button_configurations.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.button_help.setText(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.button_about.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o 1.0/2023", None))
        self.button_menu.setText("")
        self.label_menu.setText(QCoreApplication.translate("MainWindow", u" MENU", None))
        self.label_logo.setText("")
        self.button_minimize.setText("")
        self.button_restore.setText("")
        self.button_close.setText("")
        self.label_title_1.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_title_2.setText(QCoreApplication.translate("MainWindow", u"Destinat\u00e1rios", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Cadastrar destinat\u00e1rios</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Para realizar o cadastro de destinat\u00e1rios fa\u00e7a a importa\u00e7\u00e3o de um arquivo (.csv), para orienta\u00e7\u00e3oes referente ao leiaute e formato do arquivo acesse o menu AJUDA na barra lateral.</span></p></body></html>", None))
        self.button_search_recipients.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.label_file_path_recipients.setText(QCoreApplication.translate("MainWindow", u"Selecione um arquivo", None))
        self.button_validar.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.button_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_recipients.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Destinat\u00e1rios encontrados:</p></body></html>", None))
        ___qtablewidgetitem = self.table_recipients.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.table_recipients.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        self.label_title_3.setText(QCoreApplication.translate("MainWindow", u"Mensagens", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Cadastrar mensagens</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Para realizar o cadastro de mensagens fa\u00e7a a importa\u00e7\u00e3o de um arquivo (.html), para orienta\u00e7\u00e3oes referente ao leiaute e formato do arquivo acesse o menu AJUDA na barra lateral.</span></p></body></html>", None))
        self.button_search_message.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.label_file_path_message.setText(QCoreApplication.translate("MainWindow", u"Selecione um arquivo", None))
        self.lineEdit_message_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nome da mensagem", None))
        self.button_validar_message.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.button_cadastrar_message.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_recipients_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Mensagens cadastradas:</p></body></html>", None))
        self.button_excluir_message.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_title_4.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Autentica\u00e7\u00e3o SMTP</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Os envios do Appostman s\u00e3o realizados atrav\u00e9s do protocolo SMTP. Portanto \u00e9 necess\u00e1rio realizar a valida\u00e7\u00e3o dos dados antes de automatizar seus envios.</span></p><p><span style=\" font-size:14pt; font-weight:600;\">Preencha os dados de acordo com seu provedor de e-mail:</span></p><p><br/></p></body></html>", None))
        self.lineEdit_smtp_servidor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Servidor", None))
        self.lineEdit_smtp_porta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Porta", None))
        self.lineEdit_smtp_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lineEdit_smtp_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.button_smtp_validate.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_smtp), QCoreApplication.translate("MainWindow", u"SMTP", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Autentica\u00e7\u00e3o IMAP</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">A leitura dos e-mails do Appostman s\u00e3o realizadass atrav\u00e9s do protocolo IMAP. Portanto \u00e9 necess\u00e1rio realizar a valida\u00e7\u00e3o dos dados antes de automatizar seus envios.</span></p><p><span style=\" font-size:14pt; font-weight:600;\">Preencha os dados de acordo com seu provedor de e-mail:</span></p><p><br/></p></body></html>", None))
        self.lineEdit_imap_servidor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Servidor", None))
        self.lineEdit_imap_porta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Porta", None))
        self.lineEdit_imap_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lineEdit_smtp_senha_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.button_imap_validate.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_imap), QCoreApplication.translate("MainWindow", u"IMAP", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Adicionar campanha</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Dia</span></p></body></html>", None))
        self.comboBox_dia.setItemText(0, QCoreApplication.translate("MainWindow", u"Segunda-Feira", None))
        self.comboBox_dia.setItemText(1, QCoreApplication.translate("MainWindow", u"Ter\u00e7a-Feira", None))
        self.comboBox_dia.setItemText(2, QCoreApplication.translate("MainWindow", u"Quarta-Feira", None))
        self.comboBox_dia.setItemText(3, QCoreApplication.translate("MainWindow", u"Quinta-Feira", None))
        self.comboBox_dia.setItemText(4, QCoreApplication.translate("MainWindow", u"Sexta-Feira", None))
        self.comboBox_dia.setItemText(5, QCoreApplication.translate("MainWindow", u"S\u00e1bado", None))
        self.comboBox_dia.setItemText(6, QCoreApplication.translate("MainWindow", u"Domingo", None))

        self.comboBox_dia.setCurrentText(QCoreApplication.translate("MainWindow", u"Segunda-Feira", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hor\u00e1rio</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">G\u00eanero alvo</span></p></body></html>", None))
        self.comboBox_genero.setItemText(0, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.comboBox_genero.setItemText(1, QCoreApplication.translate("MainWindow", u"Feminino", None))
        self.comboBox_genero.setItemText(2, QCoreApplication.translate("MainWindow", u"Todos", None))

        self.checkBox_idade.setText(QCoreApplication.translate("MainWindow", u"Filtrar por idade", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">at\u00e9</span></p></body></html>", None))
        self.checkBox_pais.setText(QCoreApplication.translate("MainWindow", u"Filtrar por pa\u00eds", None))
        self.lineEdit_codigoPais.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do pa\u00eds", None))
        self.button_imap_validate_2.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.label_recipients_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Campanhas em funcionamento</span></p></body></html>", None))
        self.button_excluir_message_5.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_envios), QCoreApplication.translate("MainWindow", u"Envios", None))
        self.label_title_5.setText(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.label_title_6.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_copyright.setText(QCoreApplication.translate("MainWindow", u"Copyright Appostman Co.", None))
    # retranslateUi

