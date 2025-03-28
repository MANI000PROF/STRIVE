# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextBrowser,
    QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1034, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(91, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	border-radius:10px;\n"
"	background-color: rgb(102, 60, 165);\n"
"}\n"
"QPushButton{\n"
"	border:none;\n"
"	border-radius:3px;\n"
"}\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(240, 234, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(227, 221, 255);\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_10.setSpacing(30)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 30, 10, 20)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(81, 71))
        self.label_4.setPixmap(QPixmap(u":/images/Profile-Avatar-PNG.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(50)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/images/dashboard.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setIconSize(QSize(25, 25))
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.dashboard_1)

        self.notifications_1 = QPushButton(self.icon_only_widget)
        self.notifications_1.setObjectName(u"notifications_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/notifications.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.notifications_1.setIcon(icon1)
        self.notifications_1.setIconSize(QSize(25, 25))
        self.notifications_1.setCheckable(True)
        self.notifications_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.notifications_1)

        self.new_1 = QPushButton(self.icon_only_widget)
        self.new_1.setObjectName(u"new_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/news_741867.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_1.setIcon(icon2)
        self.new_1.setIconSize(QSize(36, 52))
        self.new_1.setCheckable(True)
        self.new_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.new_1)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 254, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(30)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/settings.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_1.setIcon(icon3)
        self.settings_1.setIconSize(QSize(25, 25))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.icon_only_widget)
        self.signout_1.setObjectName(u"signout_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/signout.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.signout_1.setIcon(icon4)
        self.signout_1.setIconSize(QSize(25, 25))
        self.signout_1.setCheckable(True)
        self.signout_1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.signout_1)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)


        self.gridLayout_9.addWidget(self.icon_only_widget, 0, 0, 2, 1)

        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(231, 0))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"\n"
"	color:white;\n"
"	background-color: rgb(102, 60, 165);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 30, 15, 20)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(81, 71))
        self.label_2.setPixmap(QPixmap(u":/images/Profile-Avatar-PNG.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(Qt.PlainText)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(57)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 20, 10, 0)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.dashboard_2.setFont(font1)
        self.dashboard_2.setStyleSheet(u"QPushButton{\n"
"	padding-right:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-radius:3px;\n"
"}")
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.dashboard_2)

        self.notifications_2 = QPushButton(self.icon_text_widget)
        self.notifications_2.setObjectName(u"notifications_2")
        self.notifications_2.setFont(font1)
        self.notifications_2.setStyleSheet(u"QPushButton{\n"
"	padding-right:5px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"	color:black;\n"
"\n"
"}")
        self.notifications_2.setIcon(icon1)
        self.notifications_2.setIconSize(QSize(25, 25))
        self.notifications_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.notifications_2)

        self.news_2 = QPushButton(self.icon_text_widget)
        self.news_2.setObjectName(u"news_2")
        self.news_2.setFont(font1)
        self.news_2.setStyleSheet(u"QPushButton{\n"
"	padding-right:35px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-radius:3px;\n"
"}")
        self.news_2.setIcon(icon2)
        self.news_2.setIconSize(QSize(25, 25))
        self.news_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.news_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 147, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setFont(font1)
        self.settings_2.setStyleSheet(u"QPushButton{\n"
"	padding-right:35px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-radius:3px;\n"
"}")
        self.settings_2.setIcon(icon3)
        self.settings_2.setIconSize(QSize(25, 25))
        self.settings_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.icon_text_widget)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setFont(font1)
        self.signout_2.setStyleSheet(u"QPushButton{\n"
"	padding-right:35px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-radius:3px;\n"
"}")
        self.signout_2.setIcon(icon4)
        self.signout_2.setIconSize(QSize(25, 25))
        self.signout_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.signout_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)


        self.gridLayout_9.addWidget(self.icon_text_widget, 0, 1, 2, 1)

        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, -1, -1, -1)
        self.menu_2 = QPushButton(self.header_widget)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setMaximumSize(QSize(52, 42))
        self.menu_2.setStyleSheet(u"border:none;")
        icon5 = QIcon()
        icon5.addFile(u":/images/menu.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_2.setIcon(icon5)
        self.menu_2.setIconSize(QSize(35, 35))
        self.menu_2.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.menu_2)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setUnderline(True)
        self.label_5.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_5)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(184, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.searchbar = QLineEdit(self.header_widget)
        self.searchbar.setObjectName(u"searchbar")
        self.searchbar.setStyleSheet(u"QLineEdit{\n"
"	padding-left:20px;\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color:black;\n"
"}")
        self.searchbar.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.searchbar)

        self.label_8 = QLabel(self.header_widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(32, 32))
        self.label_8.setPixmap(QPixmap(u":/images/search.ico"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_8)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_8)


        self.gridLayout_9.addWidget(self.header_widget, 0, 2, 1, 1)

        self.main_screen_widget = QWidget(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(500, 400))
        self.main_screen_widget.setMaximumSize(QSize(16777215, 16777215))
        self.main_screen_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(224, 217, 255);\n"
"	color:black;\n"
"	border-radius:10px;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.main_screen_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.gridLayout_8 = QGridLayout(self.dashboard_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.dashboard_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(170, 70))
        font3 = QFont()
        font3.setFamilies([u"Palatino Linotype"])
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setUnderline(True)
        self.label_10.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.label_20 = QLabel(self.dashboard_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(60, 40))
        self.label_20.setMaximumSize(QSize(70, 50))
        self.label_20.setTextFormat(Qt.AutoText)
        self.label_20.setPixmap(QPixmap(u":/images/dashboard.png"))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_20)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)

        self.frame_7 = QFrame(self.dashboard_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(580, 460))
        self.frame_7.setMaximumSize(QSize(900, 700))
        self.frame_7.setStyleSheet(u"background-color: rgb(243, 231, 255);\n"
"color:black;\n"
"border-radius:15px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_7)


        self.gridLayout_8.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.notifications_page = QWidget()
        self.notifications_page.setObjectName(u"notifications_page")
        self.gridLayout_7 = QGridLayout(self.notifications_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.notifications_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(180, 80))
        self.label_9.setFont(font3)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_21 = QLabel(self.notifications_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(70, 50))
        self.label_21.setMaximumSize(QSize(80, 60))
        self.label_21.setPixmap(QPixmap(u":/images/notification.png"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_21)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.frame_8 = QFrame(self.notifications_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(580, 460))
        self.frame_8.setMaximumSize(QSize(900, 700))
        self.frame_8.setStyleSheet(u"background-color: rgb(243, 231, 255);\n"
"color:black;\n"
"border-radius:15px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(50, -1, 50, 15)
        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(300, 25))
        font4 = QFont()
        font4.setFamilies([u"Palatino Linotype"])
        font4.setPointSize(10)
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	padding-right:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-radius:3px;\n"
"}")
        self.pushButton_4.setCheckable(True)

        self.verticalLayout_11.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(300, 25))
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	padding-right:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-radius:3px;\n"
"}")
        self.pushButton_5.setCheckable(True)

        self.verticalLayout_11.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(300, 25))
        self.pushButton_6.setFont(font4)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	padding-right:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-radius:3px;\n"
"}")
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_11.addWidget(self.pushButton_6)


        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_8)


        self.gridLayout_7.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.notifications_page)
        self.news_page = QWidget()
        self.news_page.setObjectName(u"news_page")
        self.gridLayout_2 = QGridLayout(self.news_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(self.news_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(250, 80))
        self.label_14.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_14)

        self.label_18 = QLabel(self.news_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(80, 70))
        self.label_18.setPixmap(QPixmap(u":/images/news_741867.png"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_18)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.frame_5 = QFrame(self.news_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(400, 300))
        self.frame_5.setMaximumSize(QSize(900, 700))
        self.frame_5.setStyleSheet(u"background-color: rgb(243, 231, 255);\n"
"color:black;\n"
"border-radius:15px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 40))
        self.label_12.setMaximumSize(QSize(16777215, 40))
        self.label_12.setFont(font4)
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-radius:10px;")
        self.label_12.setTextFormat(Qt.AutoText)
        self.label_12.setMargin(0)

        self.verticalLayout.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.verticalLayout.addWidget(self.label_13)

        self.textBrowser = QTextBrowser(self.frame_5)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-radius:10px;")

        self.verticalLayout.addWidget(self.textBrowser)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.news_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.gridLayout_5 = QGridLayout(self.settings_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_24 = QLabel(self.settings_page)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(70, 60))
        self.label_24.setMaximumSize(QSize(80, 70))
        font5 = QFont()
        font5.setFamilies([u"Palatino Linotype"])
        font5.setPointSize(18)
        font5.setBold(True)
        self.label_24.setFont(font5)
        self.label_24.setPixmap(QPixmap(u":/images/settings.png"))
        self.label_24.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_24)

        self.label_25 = QLabel(self.settings_page)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(150, 70))
        self.label_25.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_25)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.frame_6 = QFrame(self.settings_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(580, 460))
        self.frame_6.setMaximumSize(QSize(900, 700))
        self.frame_6.setStyleSheet(u"\n"
"background-color: rgb(243, 231, 255);\n"
"color:black;\n"
"border-radius:15px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(180)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(40, -1, 40, -1)
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(170, 25))
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	padding-right:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-radius:3px;\n"
"}")
        self.pushButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(170, 25))
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	padding-right:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-radius:3px;\n"
"}")
        self.pushButton_2.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(170, 25))
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	padding-right:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-radius:3px;\n"
"}")
        self.pushButton_3.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.line = QFrame(self.frame_6)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 2))
        self.line.setMaximumSize(QSize(16777215, 2))
        font6 = QFont()
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        self.line.setFont(font6)
        self.line.setStyleSheet(u"background-color: rgb(21, 21, 21);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 40))
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setFont(font4)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-radius:10px;")
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setMargin(0)

        self.verticalLayout_3.addWidget(self.label_6)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.settings_page)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.main_screen_widget, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_2.toggled.connect(self.icon_text_widget.setHidden)
        self.menu_2.toggled.connect(self.icon_only_widget.setVisible)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.notifications_2.toggled.connect(self.notifications_1.setChecked)
        self.news_2.toggled.connect(self.new_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(self.signout_1.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.notifications_1.toggled.connect(self.notifications_2.setChecked)
        self.new_1.toggled.connect(self.news_2.setChecked)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.signout_1.toggled.connect(self.signout_2.setChecked)
        self.signout_2.toggled.connect(MainWindow.close)
        self.signout_1.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.notifications_1.setText("")
        self.new_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.notifications_2.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.news_2.setText(QCoreApplication.translate("MainWindow", u"News", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.signout_2.setText(QCoreApplication.translate("MainWindow", u"SignOut", None))
        self.menu_2.setText("")
        self.label_5.setText("")
        self.searchbar.setText("")
        self.searchbar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search here....", None))
        self.label_8.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.label_20.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_21.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Enable notifications", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Notification Style", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Tone Style", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"News and Alerts", None))
        self.label_18.setText("")
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"News&Updates", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_6.setText("")
    # retranslateUi

