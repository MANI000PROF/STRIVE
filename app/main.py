from PySide6.QtWidgets import QApplication
from frontPage import MySideBar
from frontPage2 import MySideBar2
import sys
import customtkinter
from customtkinter import *
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

app = CTk()
app.title('Strive')
app.geometry('1099x754+50+0')
app.config(bg='#001220')
app.minsize(1099, 754)

font1 = ('Helvetica', 30, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL,
        password TEXT NOT NULL
        )
    ''')
def check_username(username):

  cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
  count = cursor.fetchone()[0]
  return count > 0

def signup():

    username = username_entry.get()
    password = password_entry.get()
    repassword = password_reentry.get()

    flag = check_username(username)

    if username != '' and password != '' and password == repassword:
        if flag is True:
            messagebox.showerror('Error', 'username already exists.')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            print(hashed_password)
            cursor.execute('INSERT INTO users VALUES(?, ?)', [username, hashed_password])
            conn.commit()
            messagebox.showinfo('Success', 'Account has been created.')
    else:
        if password != repassword:
            messagebox.showerror('Error', 'Re-enter the password correctly.')
        else:
            messagebox.showerror('Error', 'Enter all the data.')


def login_account():
    username = username_entry1.get()
    password = password_entry1.get()

    if username != '' and password != '':
        if username in ['manikanta', 'ironfist']:
            cursor.execute('SELECT password FROM users WHERE username =?', [username])
            result = cursor.fetchone()
            if result:
                if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                    messagebox.showinfo('Success', 'Logged in successfully.')
                    app.destroy()

                    root = QApplication(sys.argv)
                    window = MySideBar()
                    window.show()
                    root.exec()

                else:
                    messagebox.showerror('Error', 'Invalid password.')
            else:
                messagebox.showerror('Error', 'Invalid Username.')
        else:
            cursor.execute('SELECT password FROM users WHERE username =?', [username])
            result = cursor.fetchone()
            if result:
                if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                    messagebox.showinfo('Success', 'Logged in successfully.')
                    app.destroy()

                    root = QApplication(sys.argv)
                    window = MySideBar2()
                    window.show()
                    root.exec()
                else:
                    messagebox.showerror('Error', 'Invalid password.')
            else:
                messagebox.showerror('Error', 'Invalid Username.')
    else:
        messagebox.showerror('Error', 'Enter all the data.')

def login():
    frame1.destroy()
    frame2 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=1099, height=754)
    frame2.place(x=0, y=0)

    image1 = CTkImage(dark_image=Image.open("bg1.jpg"), size=(1099, 754))
    image1_label = CTkLabel(frame2, text='', image=image1)
    image1_label.place(x=0, y=0)

    login_label1 = CTkLabel(frame2, font= font1, text='Log in', text_color='#011526', bg_color= "#e0d1a6")
    login_label1.place(x=503, y=20)

    global username_entry1
    global  password_entry1

    username_entry1 = CTkEntry(frame2, font= font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_width=3, border_color='#004780', placeholder_text='Username', placeholder_text_color='#a3a3a3', width=200, height=50)
    username_entry1.place(x=450, y=80)

    password_entry1 = CTkEntry(frame2, font= font2, show= '*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200, height=50)
    password_entry1.place(x=450, y=150)

    login_button1 = CTkButton(frame2, command=login_account, font=font4,  text_color='#0c0e29', text='Login', fg_color='#a682ab', hover_color='#8b109c', bg_color='#e3d19d', cursor= 'hand2', corner_radius= 15, width=80)
    login_button1.place(x=505, y=250)

frame1 = CTkFrame(app, bg_color='#001220', fg_color='#001220', width=1099, height=754)
frame1.place(x=0, y=0)

image1 = CTkImage(dark_image=Image.open("loginbg.jpg"), size=(1099, 754))
image1_label = CTkLabel(frame1, text='', image = image1)
image1_label.place(x=0, y=0)

signup_label = CTkLabel(frame1, font=font1, text='Sign Up', text_color='#04021c',bg_color='#d5e5f7')
signup_label.place(x=490, y=20)

username_entry = CTkEntry(frame1, font=font2, text_color='#fff',fg_color='#001a2e', bg_color='#d5e5f7', border_color= '#004780', border_width= 3, placeholder_text='Username', placeholder_text_color='#a3a3a3',corner_radius=5, width=200, height=50)
username_entry.place(x=450, y=80)

password_entry = CTkEntry(frame1, font=font2, show='*', text_color='#fff',fg_color='#001a2e', bg_color= '#d5e5f7', border_color= '#004780', border_width= 3, placeholder_text='Password', placeholder_text_color='#a3a3a3',corner_radius=5, width=200, height=50 )
password_entry.place(x=450, y=150)

password_reentry = CTkEntry(frame1, font=font2, show='*', text_color='#fff',fg_color='#001a2e', bg_color= '#d5e5f7', border_color= '#004780', border_width= 3, placeholder_text='Confirm Password', placeholder_text_color='#a3a3a3',corner_radius=5, width=200, height=50 )
password_reentry.place(x=450, y=220)

signup_button = CTkButton(frame1, command=signup, font=font2, text='Sign Up', fg_color='#00965d', hover_color='#006e44', cursor= 'hand2',bg_color='#d5e5f7', corner_radius=10, width=120)
signup_button.place(x=480, y=290)

login_label = CTkLabel(frame1, font=font3, text= 'Already have an account?', text_color='#1d0342', bg_color='#d5e5f7')
login_label.place(x=440, y=380)

login_button = CTkButton(frame1, command= login, font=font4,  text_color='#00bf77', text='Login', fg_color='#c8d5e3', hover_color='#a6bae3', bg_color='#d5e5f7', cursor= 'hand2', width=40)
login_button.place(x=600, y=380)

app.mainloop()
