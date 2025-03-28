# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'index.ui'
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1238, 858)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(91, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	border-radius:10px;\n"
"	background-color: rgb(101, 4, 197);\n"
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
        self.verticalLayout_7.setSpacing(30)
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

        self.testing_1 = QPushButton(self.icon_only_widget)
        self.testing_1.setObjectName(u"testing_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/testing_4694494.png", QSize(), QIcon.Normal, QIcon.Off)
        self.testing_1.setIcon(icon2)
        self.testing_1.setIconSize(QSize(35, 30))
        self.testing_1.setCheckable(True)
        self.testing_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.testing_1)

        self.surveillance_1 = QPushButton(self.icon_only_widget)
        self.surveillance_1.setObjectName(u"surveillance_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/surveillance.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.surveillance_1.setIcon(icon3)
        self.surveillance_1.setIconSize(QSize(30, 30))
        self.surveillance_1.setCheckable(True)
        self.surveillance_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.surveillance_1)

        self.new_1 = QPushButton(self.icon_only_widget)
        self.new_1.setObjectName(u"new_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/news_741867.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_1.setIcon(icon4)
        self.new_1.setIconSize(QSize(36, 52))
        self.new_1.setCheckable(True)
        self.new_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.new_1)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 254, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon5 = QIcon()
        icon5.addFile(u":/images/settings.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_1.setIcon(icon5)
        self.settings_1.setIconSize(QSize(25, 25))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.icon_only_widget)
        self.signout_1.setObjectName(u"signout_1")
        icon6 = QIcon()
        icon6.addFile(u":/images/signout.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.signout_1.setIcon(icon6)
        self.signout_1.setIconSize(QSize(25, 25))
        self.signout_1.setCheckable(True)
        self.signout_1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.signout_1)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(231, 0))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	color:white;\n"
"	background-color: rgb(101, 4, 197);\n"
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
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 10, 0)
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

        self.testing = QFrame(self.icon_text_widget)
        self.testing.setObjectName(u"testing")
        self.testing.setFrameShape(QFrame.StyledPanel)
        self.testing.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.testing)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.testing_2 = QPushButton(self.testing)
        self.testing_2.setObjectName(u"testing_2")
        self.testing_2.setFont(font1)
        self.testing_2.setStyleSheet(u"QPushButton{\n"
"	padding-right: 25px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	\n"
"	border-radius:3px;\n"
"}")
        self.testing_2.setIcon(icon2)
        self.testing_2.setIconSize(QSize(25, 25))
        self.testing_2.setCheckable(True)

        self.verticalLayout_3.addWidget(self.testing_2)

        self.testing_dropdown = QFrame(self.testing)
        self.testing_dropdown.setObjectName(u"testing_dropdown")
        self.testing_dropdown.setFrameShape(QFrame.StyledPanel)
        self.testing_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.testing_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.test_video = QPushButton(self.testing_dropdown)
        self.test_video.setObjectName(u"test_video")
        font2 = QFont()
        font2.setPointSize(9)
        self.test_video.setFont(font2)
        self.test_video.setStyleSheet(u"QPushButton{\n"
"	padding-right:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#12B298\n"
"}")
        self.test_video.setCheckable(True)

        self.verticalLayout.addWidget(self.test_video)

        self.test_image = QPushButton(self.testing_dropdown)
        self.test_image.setObjectName(u"test_image")
        self.test_image.setFont(font2)
        self.test_image.setStyleSheet(u"QPushButton{\n"
"	padding-left:15x;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#12B298\n"
"}")
        self.test_image.setCheckable(True)

        self.verticalLayout.addWidget(self.test_image)


        self.verticalLayout_3.addWidget(self.testing_dropdown)


        self.verticalLayout_5.addWidget(self.testing)

        self.surveillance = QFrame(self.icon_text_widget)
        self.surveillance.setObjectName(u"surveillance")
        self.surveillance.setFrameShape(QFrame.StyledPanel)
        self.surveillance.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.surveillance)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.surveillance_2 = QPushButton(self.surveillance)
        self.surveillance_2.setObjectName(u"surveillance_2")
        self.surveillance_2.setFont(font1)
        self.surveillance_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:0px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"\n"
"	border-radius:3px;\n"
"}")
        self.surveillance_2.setIcon(icon3)
        self.surveillance_2.setIconSize(QSize(25, 25))
        self.surveillance_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.surveillance_2)

        self.frame_2 = QFrame(self.surveillance)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.add_camera = QPushButton(self.frame_2)
        self.add_camera.setObjectName(u"add_camera")
        self.add_camera.setFont(font2)
        self.add_camera.setStyleSheet(u"QPushButton{\n"
"	padding-right:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#12B298\n"
"}")
        self.add_camera.setCheckable(True)

        self.verticalLayout_2.addWidget(self.add_camera)

        self.cam_list = QPushButton(self.frame_2)
        self.cam_list.setObjectName(u"cam_list")
        self.cam_list.setFont(font2)
        self.cam_list.setStyleSheet(u"QPushButton{\n"
"	padding-right:50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#12B298\n"
"}")
        self.cam_list.setCheckable(True)

        self.verticalLayout_2.addWidget(self.cam_list)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_5.addWidget(self.surveillance)

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
        self.news_2.setIcon(icon4)
        self.news_2.setIconSize(QSize(25, 25))
        self.news_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.news_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 147, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(15)
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
        self.settings_2.setIcon(icon5)
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
        self.signout_2.setIcon(icon6)
        self.signout_2.setIconSize(QSize(25, 25))
        self.signout_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.signout_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setMaximumSize(QSize(52, 42))
        self.menu.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/images/menu.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon7)
        self.menu.setIconSize(QSize(35, 35))
        self.menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu)

        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setUnderline(True)
        self.label.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(184, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left:20px;\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color:black;\n"
"}")
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_7 = QLabel(self.header_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(32, 32))
        self.label_7.setPixmap(QPixmap(u":/images/search.ico"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_7)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_11.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(800, 400))
        self.main_screen_widget.setMaximumSize(QSize(1200, 550))
        self.main_screen_widget.setStyleSheet(u"background-color: rgb(249, 231, 255);")
        self.gridLayout_4 = QGridLayout(self.main_screen_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(800, 500))

        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.gridLayout_7 = QGridLayout(self.dashboard_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.dashboard_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(700, 50))
        font4 = QFont()
        font4.setFamilies([u"Palatino Linotype"])
        font4.setPointSize(18)
        font4.setBold(True)
        self.label_8.setFont(font4)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.label_20 = QLabel(self.dashboard_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(60, 40))
        self.label_20.setMaximumSize(QSize(70, 50))
        self.label_20.setTextFormat(Qt.AutoText)
        self.label_20.setPixmap(QPixmap(u":/images/dashboard.png"))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_20)

        self.verticalLayout_21.addLayout(self.horizontalLayout_9)

        self.widget = QWidget(self.dashboard_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(700, 400))
        self.widget.setMaximumSize(QSize(900, 500))
        self.widget.setStyleSheet(u"background-color: rgb(219, 201, 255);\n"
                                  "border-radius:15px;\n"
                                  "color:black;")
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        font5 = QFont()
        font5.setFamilies([u"Palatino Linotype"])
        font5.setPointSize(15)
        font5.setBold(False)
        self.label_22.setFont(font5)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_22)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(650, 2))
        self.line.setMaximumSize(QSize(900, 2))
        font6 = QFont()
        font6.setPointSize(8)
        self.line.setFont(font6)
        self.line.setStyleSheet(u"background-color: rgb(11, 11, 11);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        font7 = QFont()
        font7.setFamilies([u"Palatino Linotype"])
        font7.setPointSize(11)
        font7.setBold(False)
        self.label_23.setFont(font7)

        self.horizontalLayout_11.addWidget(self.label_23)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font7)
        self.label_27.setStyleSheet(u"border-radius:5px;\n"
                                    "background-color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.label_27)

        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font7)

        self.horizontalLayout_11.addWidget(self.label_24)

        self.detected_label = QLabel(self.widget)
        self.detected_label.setObjectName(u"detected_label")
        self.detected_label.setFont(font7)
        self.detected_label.setStyleSheet(u"border-radius:5px;\n"
                                          "background-color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.detected_label)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font7)

        self.horizontalLayout_11.addWidget(self.label_25)

        self.system_uptime_label = QLabel(self.widget)
        self.system_uptime_label.setObjectName(u"system_uptime_label")
        self.system_uptime_label.setFont(font7)
        self.system_uptime_label.setStyleSheet(u"border-radius:5px;\n"
                                               "background-color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.system_uptime_label)

        self.verticalLayout_19.addLayout(self.horizontalLayout_11)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(650, 2))
        self.line_2.setMaximumSize(QSize(900, 2))
        self.line_2.setFont(font6)
        self.line_2.setStyleSheet(u"background-color: rgb(11, 11, 11);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_2)

        self.verticalLayout_20.addLayout(self.verticalLayout_19)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 50))
        self.label_29.setMaximumSize(QSize(16777215, 50))
        font8 = QFont()
        font8.setFamilies([u"Palatino Linotype"])
        font8.setPointSize(14)
        font8.setBold(False)
        self.label_29.setFont(font8)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_29)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(650, 2))
        self.line_3.setMaximumSize(QSize(900, 2))
        self.line_3.setFont(font6)
        self.line_3.setStyleSheet(u"background-color: rgb(11, 11, 11);")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_18.addWidget(self.line_3)

        self.tableWidget_2 = QTableWidget(self.widget)
        if (self.tableWidget_2.columnCount() < 2):
                self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(550, 100))
        self.tableWidget_2.setMaximumSize(QSize(900, 150))
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(False)
        self.tableWidget_2.setFont(font9)
        #self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_2.setDragEnabled(False)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(249)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_18.addWidget(self.tableWidget_2)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(650, 2))
        self.line_4.setMaximumSize(QSize(900, 2))
        self.line_4.setFont(font6)
        self.line_4.setStyleSheet(u"background-color: rgb(11, 11, 11);")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_18.addWidget(self.line_4)

        self.verticalLayout_20.addLayout(self.verticalLayout_18)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 40))
        self.label_30.setMaximumSize(QSize(16777215, 40))
        self.label_30.setFont(font8)
        self.label_30.setLayoutDirection(Qt.RightToLeft)
        self.label_30.setScaledContents(True)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_30)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 3):
                self.tableWidget.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(550, 100))
        self.tableWidget.setMaximumSize(QSize(900, 170))
        self.tableWidget.setFont(font9)
        #self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_17.addWidget(self.tableWidget)

        self.verticalLayout_20.addLayout(self.verticalLayout_17)

        self.gridLayout_6.addLayout(self.verticalLayout_20, 0, 0, 1, 1)

        self.verticalLayout_21.addWidget(self.widget)

        self.gridLayout_7.addLayout(self.verticalLayout_21, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.dashboard_page)

        self.notifications_page = QWidget()
        self.notifications_page.setObjectName(u"notifications_page")
        self.gridLayout_8 = QGridLayout(self.notifications_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.notifications_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_21 = QLabel(self.notifications_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(70, 50))
        self.label_21.setMaximumSize(QSize(80, 60))
        self.label_21.setPixmap(QPixmap(u":/images/notification.png"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_21)

        self.verticalLayout_23.addLayout(self.horizontalLayout_10)

        self.widget_2 = QWidget(self.notifications_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(700, 400))
        self.widget_2.setMaximumSize(QSize(900, 500))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                    "border-radius:15px;\n"
                                    "color:black;")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(25)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.notifications_table = QTableWidget(self.widget_2)
        self.notifications_table.setObjectName(u"notifications_table")
        self.notifications_table.setStyleSheet(u"background-color: rgb(219, 201, 255);")

        self.verticalLayout_22.addWidget(self.notifications_table)

        self.clear_button = QPushButton(self.widget_2)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMinimumSize(QSize(50, 30))
        self.clear_button.setMaximumSize(QSize(150, 50))
        font10 = QFont()
        font10.setFamilies([u"Palatino Linotype"])
        font10.setPointSize(10)
        self.clear_button.setFont(font10)
        self.clear_button.setStyleSheet(u"QPushButton{\n"
                                        "	color:black;\n"
                                        "	border-radius:10px;\n"
                                        "	background-color: rgb(255, 138, 138);\n"
                                        "}\n"
                                        "QPushButton:checked{\n"
                                        "	background-color: rgb(255, 84, 69);\n"
                                        "	color:black;\n"
                                        "	border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "	color:white\n"
                                        "}")
        self.clear_button.setCheckable(True)

        self.verticalLayout_22.addWidget(self.clear_button)

        self.gridLayout_2.addLayout(self.verticalLayout_22, 0, 0, 1, 1)

        self.verticalLayout_23.addWidget(self.widget_2)

        self.gridLayout_8.addLayout(self.verticalLayout_23, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.notifications_page)

        self.test_video_page = QWidget()
        self.test_video_page.setObjectName(u"test_video_page")
        self.label_10 = QLabel(self.test_video_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 10, 201, 41))
        self.label_10.setFont(font4)
        self.widget3 = QWidget(self.test_video_page)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(100, 110, 602, 546))
        self.verticalLayout_12 = QVBoxLayout(self.widget3)
        self.verticalLayout_12.setSpacing(50)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.upload_video = QPushButton(self.widget3)
        self.upload_video.setObjectName(u"upload_video")
        self.upload_video.setMinimumSize(QSize(120, 40))
        self.upload_video.setMaximumSize(QSize(120, 40))
        font5 = QFont()
        font5.setFamilies([u"Palatino Linotype"])
        font5.setPointSize(11)
        self.upload_video.setFont(font5)
        self.upload_video.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"	background-color: rgb(153, 101, 189);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(168, 105, 179);\n"
"}")
        self.upload_video.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.upload_video)

        self.testVideo = QPushButton(self.widget3)
        self.testVideo.setObjectName(u"testVideo")
        self.testVideo.setMinimumSize(QSize(120, 40))
        self.testVideo.setMaximumSize(QSize(120, 40))
        font5 = QFont()
        font5.setFamilies([u"Palatino Linotype"])
        font5.setPointSize(11)
        self.testVideo.setFont(font5)
        self.testVideo.setStyleSheet(u"QPushButton{\n"
                                        "	border-radius:10px;\n"
                                        "	background-color: rgb(153, 101, 189);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:checked{\n"
                                        "	\n"
                                        "	background-color: rgb(168, 105, 179);\n"
                                        "}")
        self.testVideo.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.testVideo)

        self.label_5 = QLabel(self.widget3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 40))
        self.label_5.setMaximumSize(QSize(16777215, 40))
        font6 = QFont()
        font6.setFamilies([u"Palatino Linotype"])
        font6.setPointSize(10)
        self.label_5.setFont(font6)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-radius:10px;")
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setMargin(0)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.frame = QFrame(self.widget3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(600, 450))
        self.frame.setMaximumSize(QSize(600, 450))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame)

        self.stackedWidget.addWidget(self.test_video_page)
        self.test_image_page = QWidget()
        self.test_image_page.setObjectName(u"test_image_page")
        self.label_11 = QLabel(self.test_image_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 10, 211, 41))
        self.label_11.setFont(font4)
        self.layoutWidget_2 = QWidget(self.test_image_page)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(100, 110, 602, 546))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_15.setSpacing(50)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.upload_image = QPushButton(self.layoutWidget_2)
        self.upload_image.setObjectName(u"upload_image")
        self.upload_image.setMinimumSize(QSize(120, 40))
        self.upload_image.setMaximumSize(QSize(120, 40))
        self.upload_image.setFont(font5)
        self.upload_image.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"	background-color: rgb(153, 101, 189);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(168, 105, 179);\n"
"}")
        self.upload_image.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.upload_image)

        self.testImage = QPushButton(self.widget3)
        self.testImage.setObjectName(u"testImage")
        self.testImage.setMinimumSize(QSize(120, 40))
        self.testImage.setMaximumSize(QSize(120, 40))
        font5 = QFont()
        font5.setFamilies([u"Palatino Linotype"])
        font5.setPointSize(11)
        self.testImage.setFont(font5)
        self.testImage.setStyleSheet(u"QPushButton{\n"
                                     "	border-radius:10px;\n"
                                     "	background-color: rgb(153, 101, 189);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:checked{\n"
                                     "	\n"
                                     "	background-color: rgb(168, 105, 179);\n"
                                     "}")
        self.testImage.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.testImage)

        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 40))
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setFont(font6)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-radius:10px;")
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setMargin(0)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.verticalLayout_15.addLayout(self.horizontalLayout_7)

        self.frame_3 = QFrame(self.layoutWidget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(600, 450))
        self.frame_3.setMaximumSize(QSize(600, 450))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.test_image_page)
        self.add_cam_page = QWidget()
        self.add_cam_page.setObjectName(u"add_cam_page")
        self.label_12 = QLabel(self.add_cam_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 10, 241, 41))
        self.label_12.setFont(font4)
        self.add_new_cam = QPushButton(self.add_cam_page)
        self.add_new_cam.setObjectName(u"add_new_cam")
        self.add_new_cam.setGeometry(QRect(300, 110, 151, 41))
        font7 = QFont()
        font7.setFamilies([u"Palatino Linotype"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.add_new_cam.setFont(font7)
        self.add_new_cam.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(126, 108, 188);\n"
"	border-radius:10px;\n"
"	color:black;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(109, 99, 139);\n"
"}")
        self.add_new_cam.setCheckable(True)
        self.label_17 = QLabel(self.add_cam_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(320, -10, 100, 90))
        self.label_17.setMinimumSize(QSize(100, 90))
        self.label_17.setMaximumSize(QSize(100, 90))
        self.label_17.setPixmap(QPixmap(u":/images/surveillance.ico"))
        self.label_17.setScaledContents(True)
        self.stackedWidget.addWidget(self.add_cam_page)
        self.cam_list_page = QWidget()
        self.cam_list_page.setObjectName(u"cam_list_page")
        self.gridLayout_5 = QGridLayout(self.cam_list_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.cam_list_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.verticalLayout_13.addWidget(self.label_13)

        self.label_16 = QLabel(self.cam_list_page)
        self.label_16.setObjectName(u"label_16")
        font8 = QFont()
        font8.setFamilies([u"Palatino Linotype"])
        font8.setPointSize(8)
        font8.setBold(False)
        self.label_16.setFont(font8)

        self.verticalLayout_13.addWidget(self.label_16)


        self.gridLayout_5.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.search_camera = QLineEdit(self.cam_list_page)
        self.search_camera.setObjectName(u"search_camera")
        self.search_camera.setMinimumSize(QSize(350, 40))
        self.search_camera.setMaximumSize(QSize(400, 40))
        self.search_camera.setStyleSheet(u"QLineEdit{\n"
"	padding-left:20px;\n"
"	border:1px solid gray;\n"
"	border-radius:10px;\n"
"	color:black;\n"
"}")
        self.search_camera.setClearButtonEnabled(True)

        self.verticalLayout_14.addWidget(self.search_camera)

        self.cam_list_table = QTableWidget(self.cam_list_page)
        if (self.cam_list_table.columnCount() < 4):
            self.cam_list_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.cam_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cam_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cam_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cam_list_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.cam_list_table.setObjectName(u"cam_list_table")
        self.cam_list_table.setMinimumSize(QSize(600, 0))
        self.cam_list_table.setMaximumSize(QSize(600, 1000))
        self.cam_list_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	background-color: rgb(80, 50, 145);\n"
"	color:white;\n"
"}\n"
"QTabWidget{\n"
"	alternate-background-color:#BOEDFB;\n"
"	background-color:#F4F9FA;\n"
"	\n"
"}")
        self.cam_list_table.setAlternatingRowColors(True)

        self.verticalLayout_14.addWidget(self.cam_list_table)


        self.gridLayout_5.addLayout(self.verticalLayout_14, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.cam_list_page)

        self.news_page = QWidget()
        self.news_page.setObjectName(u"news_page")
        self.gridLayout_10 = QGridLayout(self.news_page)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.news_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_14)

        self.label_18 = QLabel(self.news_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(80, 60))
        self.label_18.setMaximumSize(QSize(80, 60))
        self.label_18.setPixmap(QPixmap(u":/images/news_741867.png"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_18)

        self.verticalLayout_24.addLayout(self.horizontalLayout_12)

        self.widget_3 = QWidget(self.news_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(700, 400))
        self.widget_3.setStyleSheet(u"QWidget{\n"
                                    "	border-radius: 15px;\n"
                                    "   color:black;\n"
                                    "	background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.gridLayout_9 = QGridLayout(self.widget_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.textBrowser = QTextBrowser(self.widget_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"background-color: rgb(219, 201, 255);\n"
                                       "color: black;")

        self.verticalLayout_16.addWidget(self.textBrowser)

        self.get_updates = QPushButton(self.widget_3)
        self.get_updates.setObjectName(u"get_updates")
        self.get_updates.setMinimumSize(QSize(200, 40))
        self.get_updates.setMaximumSize(QSize(250, 40))
        self.get_updates.setFont(font7)
        self.get_updates.setStyleSheet(u"QPushButton{\n"
                                       "	background-color: rgb(126, 108, 188);\n"
                                       "	border-radius:10px;\n"
                                       "	color:black;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:checked{\n"
                                       "	\n"
                                       "	background-color: rgb(109, 99, 139);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "	color:white;\n"
                                       "	\n"
                                       "}")
        self.get_updates.setCheckable(True)

        self.verticalLayout_16.addWidget(self.get_updates)

        self.gridLayout_9.addLayout(self.verticalLayout_16, 0, 0, 1, 1)

        self.verticalLayout_24.addWidget(self.widget_3)

        self.gridLayout_10.addLayout(self.verticalLayout_24, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.news_page)

        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.gridLayout_12 = QGridLayout(self.settings_page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(50)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_19 = QLabel(self.settings_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_19)

        self.label_15 = QLabel(self.settings_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(70, 60))
        self.label_15.setMaximumSize(QSize(80, 70))
        self.label_15.setFont(font4)
        self.label_15.setPixmap(QPixmap(u":/images/settings.png"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.verticalLayout_26.addLayout(self.horizontalLayout_8)

        self.frame_5 = QFrame(self.settings_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(700, 400))
        self.frame_5.setMaximumSize(QSize(900, 500))
        self.frame_5.setStyleSheet(u"background-color: white;\n"
                                   "color:black;\n"
                                   "border-radius:15px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(50)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.test_video_2 = QPushButton(self.frame_5)
        self.test_video_2.setObjectName(u"test_video_2")
        self.test_video_2.setMinimumSize(QSize(0, 40))
        self.test_video_2.setFont(font2)
        self.test_video_2.setStyleSheet(u"QPushButton{\n"
                                        "	padding-right:15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "	color:#12B298\n"
                                        "}")
        self.test_video_2.setCheckable(True)

        self.verticalLayout_25.addWidget(self.test_video_2)

        self.test_video_3 = QPushButton(self.frame_5)
        self.test_video_3.setObjectName(u"test_video_3")
        self.test_video_3.setMinimumSize(QSize(0, 40))
        self.test_video_3.setFont(font2)
        self.test_video_3.setStyleSheet(u"QPushButton{\n"
                                        "	padding-right:15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "	color:#12B298\n"
                                        "}")
        self.test_video_3.setCheckable(True)

        self.verticalLayout_25.addWidget(self.test_video_3)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.test_video_8 = QPushButton(self.frame_5)
        self.test_video_8.setObjectName(u"test_video_8")
        self.test_video_8.setMinimumSize(QSize(150, 50))
        self.test_video_8.setMaximumSize(QSize(200, 50))
        font14 = QFont()
        font14.setPointSize(10)
        self.test_video_8.setFont(font14)
        self.test_video_8.setStyleSheet(u"QPushButton{\n"
                                        "	padding-right:15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "	color:#12B298\n"
                                        "}")
        self.test_video_8.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.test_video_8)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 30))
        self.pushButton.setMaximumSize(QSize(90, 30))
        self.pushButton.setFont(font14)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	\n"
                                      "	background-color: rgb(211, 202, 255);\n"
                                      "	border-radius:10px;\n"
                                      "	\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "	\n"
                                      "	\n"
                                      "	color: rgb(42, 255, 138);\n"
                                      "	alternate-background-color: rgb(136, 119, 166);\n"
                                      "}\n"
                                      "QPushButton:checked{\n"
                                      "	\n"
                                      "	alternate-background-color: rgb(132, 106, 154);\n"
                                      "}")
        self.pushButton.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.pushButton)

        self.verticalLayout_25.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.test_video_12 = QPushButton(self.frame_5)
        self.test_video_12.setObjectName(u"test_video_12")
        self.test_video_12.setMinimumSize(QSize(150, 50))
        self.test_video_12.setMaximumSize(QSize(200, 50))
        self.test_video_12.setFont(font14)
        self.test_video_12.setStyleSheet(u"QPushButton{\n"
                                         "	padding-right:15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "	color:#12B298\n"
                                         "}")
        self.test_video_12.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.test_video_12)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 30))
        self.pushButton_3.setMaximumSize(QSize(90, 30))
        self.pushButton_3.setFont(font14)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
                                        "	\n"
                                        "	background-color: rgb(211, 202, 255);\n"
                                        "	border-radius:10px;\n"
                                        "	\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "	\n"
                                        "	\n"
                                        "	color: rgb(42, 255, 138);\n"
                                        "	alternate-background-color: rgb(136, 119, 166);\n"
                                        "}\n"
                                        "QPushButton:checked{\n"
                                        "	\n"
                                        "	alternate-background-color: rgb(132, 106, 154);\n"
                                        "}")
        self.pushButton_3.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.pushButton_3)

        self.verticalLayout_25.addLayout(self.horizontalLayout_13)

        self.gridLayout_11.addLayout(self.verticalLayout_25, 0, 0, 1, 1)

        self.verticalLayout_26.addWidget(self.frame_5)

        self.gridLayout_12.addLayout(self.verticalLayout_26, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.settings_page)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.verticalLayout_11.addWidget(self.main_screen_widget)

        self.gridLayout.addLayout(self.verticalLayout_11, 0, 2, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.testing_2.toggled.connect(self.testing_dropdown.setHidden)
        self.surveillance_2.toggled.connect(self.frame_2.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.notifications_2.toggled.connect(self.notifications_1.setChecked)
        self.testing_2.toggled.connect(self.testing_1.setChecked)
        self.surveillance_2.toggled.connect(self.surveillance_1.setChecked)
        self.news_2.toggled.connect(self.new_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(self.signout_1.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)
        self.menu.toggled.connect(self.icon_text_widget.setHidden)
        self.menu.toggled.connect(self.icon_only_widget.setVisible)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.notifications_1.setText("")
        self.testing_1.setText("")
        self.surveillance_1.setText("")
        self.new_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.notifications_2.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.testing_2.setText(QCoreApplication.translate("MainWindow", u"Testing", None))
        self.test_video.setText(QCoreApplication.translate("MainWindow", u"Test a video", None))
        self.test_image.setText(QCoreApplication.translate("MainWindow", u"Test an Image", None))
        self.surveillance_2.setText(QCoreApplication.translate("MainWindow", u"Surveillance", None))
        self.add_camera.setText(QCoreApplication.translate("MainWindow", u"Add a camera", None))
        self.cam_list.setText(QCoreApplication.translate("MainWindow", u"cam list", None))
        self.news_2.setText(QCoreApplication.translate("MainWindow", u"News", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.signout_2.setText(QCoreApplication.translate("MainWindow", u"SignOut", None))
        self.menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enhance the Striving Force.....", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search here....", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.label_20.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"System status", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Active Cameras:", None))
        self.label_27.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Detected Incidents:", None))
        self.detected_label.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"System Uptime: ", None))
        self.system_uptime_label.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Active Cameras", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cam", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Recent Activity", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Details", None));

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_21.setText("")
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear Notifications", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Video Testing", None))
        self.upload_video.setText(QCoreApplication.translate("MainWindow", u"Upload Video", None))
        self.testVideo.setText(QCoreApplication.translate("MainWindow", u"Testing Video", None))
        self.label_5.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Image Testing", None))
        self.upload_image.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.testImage.setText(QCoreApplication.translate("MainWindow", u"Testing Image", None))
        self.label_6.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Add a Camera", None))
        self.add_new_cam.setText(QCoreApplication.translate("MainWindow", u"Add New Camera", None))
        self.label_17.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Surveillance Cameras List", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Surveillance cameras List", None))
        self.search_camera.setText("")
        self.search_camera.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Camera", None))
        ___qtablewidgetitem = self.cam_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.cam_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Cam ID", None));
        ___qtablewidgetitem2 = self.cam_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem3 = self.cam_list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Actions", None));

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"News and Alerts", None))
        self.label_18.setText("")
        self.get_updates.setText(QCoreApplication.translate("MainWindow", u"Get Exclusive Updates", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_15.setText("")
        self.test_video_2.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.test_video_3.setText(QCoreApplication.translate("MainWindow", u"Update Profile", None))
        self.test_video_8.setText(QCoreApplication.translate("MainWindow", u"Toggle Notifications", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ON/OFF", None))
        self.test_video_12.setText(QCoreApplication.translate("MainWindow", u"Toggle Dark Mode", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"ON/OFF", None))
    # retranslateUi

