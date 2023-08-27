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
        MainWindow.resize(953, 626)
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
        self.gridLayout_2 = QGridLayout(self.frame_main_page2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.frame_main_page2)

        self.pages.addWidget(self.recipients)
        self.messages = QWidget()
        self.messages.setObjectName(u"messages")
        self.verticalLayout_12 = QVBoxLayout(self.messages)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_title_3 = QFrame(self.messages)
        self.frame_title_3.setObjectName(u"frame_title_3")
        font6 = QFont()
        font6.setFamily(u"Rockwell")
        font6.setPointSize(12)
        self.frame_title_3.setFont(font6)
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
        self.gridLayout_3 = QGridLayout(self.frame_main_page3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.frame_main_page3)

        self.pages.addWidget(self.messages)
        self.configurations = QWidget()
        self.configurations.setObjectName(u"configurations")
        self.verticalLayout_14 = QVBoxLayout(self.configurations)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
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
        self.frame_main_page4.setFrameShape(QFrame.StyledPanel)
        self.frame_main_page4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_main_page4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

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

        self.pages.setCurrentIndex(5)


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
        self.label_title_3.setText(QCoreApplication.translate("MainWindow", u"Mensagens", None))
        self.label_title_4.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label_title_5.setText(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.label_title_6.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_copyright.setText(QCoreApplication.translate("MainWindow", u"Copyright Appostman Co.", None))
    # retranslateUi

