# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Signal, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget, QMessageBox)
import mysql.connector

class updateDialog(QDialog):

    #define a custom signal as a class variable
    data_updated = Signal()

    def __init__(self, row_index, row_data):
        super().__init__()

        # store the row_index and row_data as instance variables
        self.row_index = row_index
        self.row_data = row_data

        self.cam_info = self.select_camera()[0]

        self.cam_name_info = self.cam_info[0]
        self.cam_ipAddress_info = self.cam_info[1]
        self.cam_location_info = self.cam_info[2]

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
        self.label.setGeometry(QRect(0, 30, 301, 41))
        font = QFont()
        font.setFamilies([u"Palatino Linotype"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 130, 471, 341))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Palatino Linotype"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.edit_name_lineedit = QLineEdit(self.layoutWidget)
        self.edit_name_lineedit.setObjectName(u"edit_name_lineedit")
        self.edit_name_lineedit.setMinimumSize(QSize(0, 35))
        self.edit_name_lineedit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.edit_name_lineedit)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.edit_ip_lineedit = QLineEdit(self.layoutWidget)
        self.edit_ip_lineedit.setObjectName(u"edit_ip_lineedit")
        self.edit_ip_lineedit.setMinimumSize(QSize(0, 35))
        self.edit_ip_lineedit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.edit_ip_lineedit)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.edit_location_lineedit = QLineEdit(self.layoutWidget)
        self.edit_location_lineedit.setObjectName(u"edit_location_lineedit")
        self.edit_location_lineedit.setMinimumSize(QSize(0, 35))
        self.edit_location_lineedit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.edit_location_lineedit)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(300, 490, 211, 71))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.edit_button = QPushButton(self.layoutWidget1)
        self.edit_button.setObjectName(u"edit_button")
        font2 = QFont()
        font2.setFamilies([u"Palatino Linotype"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.edit_button.setFont(font2)
        self.edit_button.setStyleSheet(u"QPushButton{\n"
        "	border-radius:10px;\n"
        "	border:none;\n"
        "	background-color: rgb(17, 225, 42);\n"
        "}\n"
        "\n"
        "QPushButton:checked{\n"
        "	background-color: rgb(28, 153, 26);\n"
        "}")
        self.edit_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.edit_button)

        self.edit_cancel_button = QPushButton(self.layoutWidget1)
        self.edit_cancel_button.setObjectName(u"edit_cancel_button")
        self.edit_cancel_button.setFont(font2)
        self.edit_cancel_button.setStyleSheet(u"QPushButton{\n"
        "	border-radius:10px;	\n"
        "	border:none;\n"
        "	background-color: rgb(254, 48, 12);\n"
        "}\n"
        "\n"
        "QPushButton:checked{\n"
        "	\n"
        "	background-color: rgb(147, 10, 5);\n"
        "}")
        self.edit_cancel_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.edit_cancel_button)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("updateDialog", u"updateCameraDialog", None))
        self.label.setText(QCoreApplication.translate("updateDialog", u"Edit Camera details", None))
        self.label_2.setText(QCoreApplication.translate("updateDialog", u"Nick  Name", None))
        self.label_3.setText(QCoreApplication.translate("updateDialog", u"IP Address", None))
        self.label_4.setText(QCoreApplication.translate("updateDialog", u"Location", None))
        self.edit_button.setText(QCoreApplication.translate("updateDialog", u"Edit", None))
        self.edit_cancel_button.setText(QCoreApplication.translate("updateDialog", u"Cancel", None))
    # retranslateUi

        self.edit_name_lineedit.setText(str(self.cam_name_info))
        self.edit_ip_lineedit.setText(str(self.cam_ipAddress_info))
        self.edit_location_lineedit.setText(str(self.cam_location_info))

        self.edit_button.clicked.connect(self.update_data)
        self.edit_cancel_button.clicked.connect(self.close)

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

    def select_camera(self):

        self.cursor = self.create_connection().cursor()

        # get students variable from tuples
        self.cam_name = self.row_data[0]
        self.ipAddress = self.row_data[1]

        params = [
            self.cam_name,
            self.ipAddress
        ]

        select_query = f"SELECT name, ipAddress, location FROM camList WHERE name=%s AND ipAddress=%s"

        self.cursor.execute(select_query, params)

        records = self.cursor.fetchall()

        self.mydb.commit()
        self.mydb.close()
        return records

    def update_data(self):

        try:
            connection = self.create_connection()

            if connection is None:
                return

            cursor = connection.cursor()

            params = (
                self.edit_name_lineedit.text(),
                self.edit_ip_lineedit.text(),
                self.edit_location_lineedit.text(),
                self.cam_name_info
            )

            # Update query
            update_query = f"UPDATE camList SET name=%s, ipAddress=%s, location=%s WHERE name=%s"

            cursor.execute(update_query, params)
            connection.commit()
            self.show_updated_message()
            cursor.close()
            connection.close()
            self.close()

            # emit the signal
            self.data_updated.emit()

        except mysql.connector.Error as err:
            # handles erros in sql query
            print(f"err : {err}")
            
    def show_updated_message(self):

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.cam_name_info + " updated into the database")
        msg_box.exec()

