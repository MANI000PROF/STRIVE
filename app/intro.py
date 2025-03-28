from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QMainWindow,
    QLineEdit, QVBoxLayout, QGridLayout, QHBoxLayout
    )
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
import sys
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

# conn = sqlite3.connect('data.db')
# cursor = conn.cursor()
#
# cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS users(
#         username TEXT NOT NULL,
#         password TEXT NOT NULL
#         )
#     ''')

class Window(QWidget):

    def display(self):
        print(self.username_entry.text())
        print(self.password_entry.text())

    def check(self):
        if self.username_entry.text() == "manikanta" and self.password.text() == "123456":
            print("Login sucessfull")
        else:
            print("Invalid Username or Password")

    def __init__(self):
        super().__init__()
        self.resize(300,300)
        self.setWindowIcon(QIcon(r'E:\PythonProjects\pythonProject\app\images\strive.png'))
        self.setWindowTitle("STRIVE")
        self.setMinimumSize(600, 500)

        p_layout = QGridLayout()
        self.setLayout(p_layout)

        image = QLabel()
        image.setPixmap(QPixmap("loginbg.jpg"))
        # self.setCentralWidget(image)

        self.username = QLabel("Username : ")
        p_layout.addWidget(self.username, 0, 0)

        self.password = QLabel("Password : ")
        p_layout.addWidget(self.password, 1, 0)

        self.username_entry = QLineEdit()
        self.username_entry.setFixedWidth(120)
        p_layout.addWidget(self.username_entry, 0, 1)

        self.password_entry = QLineEdit()
        self.password_entry.setFixedWidth(120)
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        p_layout.addWidget(self.password_entry, 1, 1)

        register = QPushButton("Register")
        register.setFixedWidth(100)
        register.clicked.connect(self.display)
        p_layout.addWidget(register, 2, 2, Qt.AlignmentFlag.AlignRight)

        login = QPushButton("Login")
        login.setFixedWidth(100)
        login.clicked.connect(self.check)
        p_layout.addWidget(login, 2, 1, Qt.AlignmentFlag.AlignLeft)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())