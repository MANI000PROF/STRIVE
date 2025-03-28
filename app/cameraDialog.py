# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameraDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget, QMessageBox)
import mysql.connector


class Ui_cameraDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(548, 589)
        self.setStyleSheet(u"QDialog{\n"
                           "	background-color:white;\n"
                           "}\n"
                           "\n"
                           "QLineEdit{\n"
                           "	border:1px solid gray;\n"
                           "	border-radius:10px;\n"
                           "	padding-left:15px;\n"
                           "	height:35px;\n"
                           "}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 79, 541, 21))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 30, 291, 41))
        font = QFont()
        font.setFamilies([u"Palatino Linotype"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 130, 471, 341))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Palatino Linotype"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.name_lineedit = QLineEdit(self.widget)
        self.name_lineedit.setObjectName(u"name_lineedit")
        self.name_lineedit.setMinimumSize(QSize(0, 35))
        self.name_lineedit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.name_lineedit)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.ip_lineedit = QLineEdit(self.widget)
        self.ip_lineedit.setObjectName(u"ip_lineedit ")
        self.ip_lineedit.setMinimumSize(QSize(0, 35))
        self.ip_lineedit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.ip_lineedit)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.location_lineedit = QLineEdit(self.widget)
        self.location_lineedit.setObjectName(u"location_lineedit")
        self.location_lineedit.setMinimumSize(QSize(0, 35))
        self.location_lineedit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.location_lineedit)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.widget1 = QWidget(self)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(300, 490, 211, 71))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_button = QPushButton(self.widget1)
        self.add_button.setObjectName(u"add_button")
        font2 = QFont()
        font2.setFamilies([u"Palatino Linotype"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.add_button.setFont(font2)
        self.add_button.setStyleSheet(u"QPushButton{\n"
                                      "	border-radius:10px;\n"
                                      "	border:none;\n"
                                      "	background-color: rgb(17, 225, 42);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:checked{\n"
                                      "	background-color: rgb(28, 153, 26);\n"
                                      "}")
        self.add_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.add_button)

        self.cancel_button = QPushButton(self.widget1)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setFont(font2)
        self.cancel_button.setStyleSheet(u"QPushButton{\n"
                                         "	border-radius:10px;	\n"
                                         "	border:none;\n"
                                         "	background-color: rgb(254, 48, 12);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:checked{\n"
                                         "	\n"
                                         "	background-color: rgb(147, 10, 5);\n"
                                         "}")
        self.cancel_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.cancel_button)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, cameraDialog):
        cameraDialog.setWindowTitle(QCoreApplication.translate("cameraDialog", u"CameraDialog", None))
        self.label.setText(QCoreApplication.translate("cameraDialog", u"Add new Camera", None))
        self.label_2.setText(QCoreApplication.translate("cameraDialog", u"Nick Name", None))
        self.label_3.setText(QCoreApplication.translate("cameraDialog", u"IP Address", None))
        self.label_4.setText(QCoreApplication.translate("cameraDialog", u"Location", None))
        self.add_button.setText(QCoreApplication.translate("cameraDialog", u"Add", None))
        self.cancel_button.setText(QCoreApplication.translate("cameraDialog", u"Cancel", None))
    # retranslateUi

    # add new pupil when you press a button
        self.add_button.clicked.connect(self.add_camera)
        self.cancel_button.clicked.connect(self.close)

    # create database connection
    def create_connection(self):
        # Replace these with actual MySQL server details
        host_name = "localhost"
        user_name = "root"
        mypassword = "Garikapadu_0836"
        database_name = "my_cameras"

        # establish connection to mySQL server
        self.mydb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=mypassword
        )
        cursor = self.mydb.cursor()

        # create database if it doesn't exists
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')

        # connect to database
        self.mydb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=mypassword,
            database=database_name
        )
        return self.mydb
    # Add new camera
    def add_new_camera(self):

        try:
            connection = self.create_connection()
            if connection is None:
                return
            cursor = connection.cursor()

            #create list for the cameras
            self.new_cam = [
                self.name_lineedit.text(),
                self.ip_lineedit.text(),
                self.location_lineedit.text()
            ]

            # to insert multiple rows in mySQL database
            insert_cam_query = f"""INSERT INTO camList (name, ipAddress, location) VALUES(%s, %s, %s)"""
            cursor.execute(insert_cam_query, self.new_cam)
            self.show_inserted_message()
            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:

            # handles errors
            print(f"Error: {err}")

    def show_inserted_message(self):

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.name_lineedit.text() + " inserted into the database")
        msg_box.exec()

    def add_camera(self):
        self.add_new_camera()
        self.accept()
