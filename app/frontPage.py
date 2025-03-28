import sys

from PySide6.QtWidgets import QMainWindow, QMenu, QTableWidgetItem, QTextEdit, QFileDialog, QWidget, QMessageBox, QDialog, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from PySide6.QtGui import QAction, QIcon
from ui_index import Ui_MainWindow
import mysql.connector
from updateDialog import updateDialog
from datetime import datetime
import winsound
import numpy as np
from ultralytics import YOLO
import cv2
import cvzone
import math
import logging
from twilio.rest import Client
import requests
import threading

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Strive")
        self.setWindowIcon(QIcon("strive.png"))

        self.filename = ""
        self.location = ""
        self.flag = True
        self.notifications = []
        self.detected = 0

    #Hide widget menu
        self.icon_text_widget.setHidden(True)

    #Hide dropdowns
        self.testing_dropdown.setHidden(True)
        self.frame_2.setHidden(True)

    #to set default page as dashboard
        self.stackedWidget.setCurrentIndex(0)

    #connect Buttons to switch pages
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.notifications_1.clicked.connect(self.switch_to_notfications_page)
        self.notifications_1.clicked.connect(self.display_notifications)
        self.notifications_2.clicked.connect(self.switch_to_notfications_page)
        self.notifications_2.clicked.connect(self.display_notifications)

        self.test_video.clicked.connect(self.switch_to_test_video_page)

        self.test_image.clicked.connect(self.switch_to_test_image_page)

        self.add_camera.clicked.connect(self.switch_to_add_camera_page)

        self.cam_list.clicked.connect(self.switch_to_cam_list_page)

        self.new_1.clicked.connect(self.switch_to_news_page)
        self.news_2.clicked.connect(self.switch_to_news_page)

        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page)

    #connect Buttons to respective context menu
        self.testing_1.clicked.connect(self.testing_context_menu)
        self.surveillance_1.clicked.connect(self.surveillance_context_menu)

    # connect to mysql server and create database if not exists
        self.create_connection()

    #create camList table
        self.create_camList_table()

    # Load camera List to QTable
        self.load_camList()
        self.search_camera.textChanged.connect(self.search_cam)

        self.lineEdit.textChanged.connect(self.search_page)

    # control column widths
        self.cam_list_table.setColumnWidth(0, 120)
        self.cam_list_table.setColumnWidth(1, 150)
        self.cam_list_table.setColumnWidth(2, 130)
        self.cam_list_table.setColumnWidth(3, 200)

    # open add cam dialog
        self.add_new_cam.clicked.connect(self.open_addCam_dialog)

    #connecting upload Video button to function
        self.upload_video.clicked.connect(self.uploadVideo)

    #connecting upload_image button to function
        self.upload_image.clicked.connect(self.uploadImage)

    # adding startdetection func to pushButtons
        self.testVideo.clicked.connect(self.startDetection)

        self.testImage.clicked.connect(self.startDetection)

        self.now = datetime.now().strftime("%Y-%m-%d   %H:%M")

        self.num = self.count_active_cameras()
        self.label_27.setText(self.num)
        self.detected_label.setText(str(self.detected))
        self.system_uptime_label.setText(self.now)

        self.clear_button.clicked.connect(self.clear_notifications)

        self.load_active_cam()

        self.initial_news()
        self.get_updates.clicked.connect(self.fetch_news)
        self.api_key = '028d43579e5447b0a0ac7f7abe4a8604'
        self.base_url = 'https://newsapi.org/v2/top-headlines'

        # Initialize theme
        self.current_theme = "Light"
        self.set_theme(self.current_theme)
        self.pushButton_3.clicked.connect(self.toggle_theme)

    def time(self):
        self.now = datetime.now().strftime("%Y-%m-%d   %H:%M")
        self.system_uptime_label.setText(self.now)

    #methods to switch different pages
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_notfications_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_test_video_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_test_image_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_add_camera_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_cam_list_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_news_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(7)

    #methods to show context menu
    def testing_context_menu(self):
        self.show_custom_context_menu(self.testing_1, ["Test a video", "Test an Image"])

    def surveillance_context_menu(self):
        self.show_custom_context_menu(self.surveillance_1, ["Add New Camera", "Camera List"])

    #set style for menu
    def show_custom_context_menu(self, button, menu_items):

        menu = QMenu(self)
        #set style sheet
        menu.setStyleSheet("""
                        QMenu{
                            background-color: black;
                            color: white;
                            }
                        QMenu:selected{
                            background-color: white;
                            color: #12B298;
                            }
                        """)
        #add actions for menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        # show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):

        text = self.sender().text()

        if text == "Test a video":
            self.switch_to_test_video_page()
        elif text == "Test an Image":
            self.switch_to_test_image_page()
        elif text == "Add New Camera":
            self.switch_to_add_camera_page()
        elif text == "Camera List":
            self.switch_to_cam_list_page()

    def check_camera(self, index, result):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            result[index] = True
            cap.release()

    def count_active_cameras(self, max_cameras=10):
        threads = []
        results = [False] * max_cameras

        for i in range(max_cameras):
            thread = threading.Thread(target=self.check_camera, args=(i, results))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        active_cameras = sum(results)
        return str(active_cameras)

    def search_page(self):
        text = self.lineEdit.text()

        if text == "notifications":
            self.switch_to_notfications_page()
        elif text == "testing":
            self.switch_to_test_video_page()
        elif text == "surveillance":
            self.switch_to_cam_list_page()
        elif text == "news":
            self.switch_to_news_page()
        elif text == "settings":
            self.switch_to_settings_page()
        else:
            self.switch_to_dashboard_page()

    def display_notifications(self):

        self.tableWidget.setRowCount(0)

        for row_index, row_data in enumerate(self.notifications):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_index, col_index, item)
                self.tableWidget.setRowHeight(row_index, 50)

    def initial_news(self):
        initial_news = """
               Welcome to the News Page!
               -------------------------

               Latest updates on our project:

               - We are launching a new feature next week.
               - Our team won an award for innovation.
               - Stay tuned for more updates!
               """
        self.textBrowser.setText(initial_news)

    def fetch_news(self):
        try:
            # Example request: Fetch top headlines from 'technology' category
            params = {
                'apiKey': self.api_key,
                'q': 'accident',  # Keyword related to accidents
                'language': 'en',
                'sortBy': 'publishedAt',
                'pageSize': 5  # Number of articles to fetch
            }
            response = requests.get(self.base_url, params=params)

            if response.status_code == 200:
                news_data = response.json()
                articles = news_data.get('articles', [])

                # Display fetched updates
                if articles:
                    update_text = "\n\nFetched Update:\n\n"
                    for article in articles[:3]:  # Displaying top 3 articles
                        update_text += f"{article['title']}\n\n{article['description']}\n\n"
                    self.textBrowser.append(update_text)
                else:
                    self.textBrowser.append("\n\nNo articles found.")
            else:
                self.textBrowser.append(f"\n\nFailed to fetch updates. Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.textBrowser.append(f"\n\nError fetching updates: {str(e)}")

    def toggle_theme(self):

        if self.current_theme == "Light":
            self.set_theme("Dark")
        else:
            self.set_theme("Light")

    def set_theme(self, theme):
        if theme == "Dark":
            self.setStyleSheet("""
                background-color: #333;
                color: #FFF;
            """)
        else:
            self.setStyleSheet("")  # Reset stylesheet to default (light mode)
        self.current_theme = theme

    def clear_notifications(self):
        self.tableWidget.setRowCount(0)
        self.notifications = []

    def reload_active_cam(self):
        self.load_active_cam()

    def load_active_cam(self):

        self.tableWidget_2.setRowCount(0)

        data = self.get_active_cam()

        for row_index, row_data in enumerate(data):
            self.tableWidget_2.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget_2.setItem(row_index, col_index, item)
                self.tableWidget_2.setRowHeight(row_index, 50)

    def get_active_cam(self):

        cursor = self.create_connection().cursor()
        query = f""" SELECT name, location FROM camlist"""

        cursor.execute(query)
        data = cursor.fetchall()
        return data

    # create database connection
    def create_connection(self):

        # Replace these with actual MySQL server details
        host_name = "localhost"
        user_name = "root"
        mypassword = "Garikapadu_0836"
        database_name = "my_cameras"

        #establish connection to mySQL server
        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = mypassword
        )
        cursor = self.mydb.cursor()

        # create database if it doesn't exists
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')

        #connect to database
        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = mypassword,
            database = database_name
        )
        return self.mydb
    # create my_cameras table
    def create_camList_table(self):

        # create cursor to execute queries
        cursor = self.create_connection().cursor()

        # the query
        create_camList_table = f"""
            CREATE TABLE IF NOT EXISTS camList(
                name TEXT,
                ipAddress INT(15) PRIMARY KEY,
                location TEXT
                )"""
        cursor.execute(create_camList_table)

        #commit the changes and close connection
        self.mydb.commit()
        self.mydb.close()

    # open dialog for adding new camera
    def open_addCam_dialog(self):

        from cameraDialog import Ui_cameraDialog

        #instantiate and show the dialog
        add_camDialog = Ui_cameraDialog(self)
        result = add_camDialog.exec() # this will block untill dialog is closed

        self.reload_camList_table()

    def reload_camList_table(self):

        self.load_camList()

    # Load camera list to QTable
    def load_camList(self):

        self.cam_list_table.setRowCount(0)

        #fetch data based on selected name of the camera
        ##selected_name = self.search_camera.text()
        data = self.get_data_from_table()

        #populate the table with filters
        for row_index, row_data in enumerate(data):
            self.cam_list_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.cam_list_table.setItem(row_index, col_index, item)

                #create custom widget with two buttons
                double_button_widget = DoubleButtonWidgetCamera(row_index, row_data, self)

                # set this custom widget with two buttons as the cell widget for the actions column
                self.cam_list_table.setCellWidget(row_index, 3, double_button_widget)
                self.cam_list_table.setRowHeight(row_index, 50)

    def get_data_from_table(self):

        cursor = self.create_connection().cursor()

        #construct query based on selected filter
        query = f""" SELECT name, ipAddress, location FROM camlist"""

        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def search_cam(self):

        #clear previous table
        self.cam_list_table.setRowCount(0)

        #Get the search query from the QLineEdit
        search_query = self.search_camera.text()

        #execute sql query
        cursor = self.create_connection().cursor()
        sql_query = f""" SELECT name, ipAddress, location FROM camList WHERE name LIKE '%{search_query}%'"""
        cursor.execute(sql_query)
        results = cursor.fetchall()

        # populate the table with filters
        for row_index, row_data in enumerate(results):
            self.cam_list_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.cam_list_table.setItem(row_index, col_index, item)

                # create custom widget with two buttons
                double_button_widget = DoubleButtonWidgetCamera(row_index, row_data, self)

                # set this custom widget with two buttons as the cell widget for the actions column
                self.cam_list_table.setCellWidget(row_index, 3, double_button_widget)
                self.cam_list_table.setRowHeight(row_index, 50)

    # beep sound for alert
    def beep(self):

        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

    # for uploadeing the video or image file

    def uploadVideo(self):
        options = QFileDialog.Option.DontUseNativeDialog
        file_filter = "Video Files (*.mp4 *.avi *.mkv)"
        self.filename, _ = QFileDialog.getOpenFileName(self, "Select Video File", "videos", file_filter,
                                                       options=options)

        if not self.filename:
            QMessageBox.critical(self, "Error", "Please select a valid video file.")
            return

        self.label_5.setText(self.filename)

    def uploadImage(self):
        options = QFileDialog.Option.DontUseNativeDialog
        file_filter = "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        self.filename, _ = QFileDialog.getOpenFileName(self, "Select Image File", "images", file_filter,
                                                       options=options)

        if not self.filename:
            QMessageBox.critical(self, "Error", "Please select a valid image file.")
            return

        self.label_6.setText(self.filename)

    def sendMessage1(self, msg):
        logging.basicConfig(level=logging.DEBUG)
        try:
            account_sid = 'ACb7039aaca077d1c7cc5a7317ecfefffe'
            auth_token = 'ee5ef9866a2b8e858f3e2bf721f3a05e'
            client = Client(account_sid, auth_token)
            twilio_number = '+13252214708'
            fire_number = '+918919698182'
            logging.debug(f"Sending message: {msg}")
            self.message = client.messages.create(
                body=msg,
                from_=twilio_number,
                to=fire_number
            )
        except Exception as e:
            logging.error(f"Failed to send message: {e}")
            QMessageBox.critical(self, "Error", f"Failed to send message: {e}")

    def sendMessage(self, msg):
        logging.basicConfig(level=logging.DEBUG)
        try:
            account_sid = 'ACbd8630478ac2f51efb0c30b385ad064e'
            auth_token = '8c93bf987205eb1729c23885601fe853'
            client = Client(account_sid, auth_token)
            twilio_number = '+17723563829'
            accident_number = '+918328628340'
            logging.debug(f"Sending message: {msg}")
            self.message = client.messages.create(
                body=msg,
                from_=twilio_number,
                to=accident_number
            )
        except Exception as e:
            logging.error(f"Failed to send message: {e}")
            QMessageBox.critical(self, "Error", f"Failed to send message: {e}")

    global flag
    global location

    def process_frame(self, model, classNames, img):
        results = model(img, conf=0.6, stream=True)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1

                # Additional check for valid dimensions
                if w > 0 and h > 0:
                    cvzone.cornerRect(img, (x1, y1, w, h))

                    # confidence
                    conf = math.ceil((box.conf[0] * 100)) / 100

                    # class name
                    cls = int(box.cls[0])
                    cvzone.putTextRect(img, f'{classNames[cls]}:{conf}', (max(0, x1), max(35, y1)), scale=0.6,
                                       thickness=1, offset=3)

                    # Check for accidents and update alert_message
                    if classNames[cls] in ["fire_accident", "vehicle_accident"]:
                        alert_message = f"Accident detected: {classNames[cls]}, Confidence: {conf}, Location: {self.location}"
                        self.notifications = alert_message

                        # If an accident is detected, send alert message
                        if alert_message:
                            print(alert_message)
                            if classNames[cls] == "fire_accident":
                                self.sendMessage(alert_message)
                            else:
                                self.sendMessage1(alert_message)
                            # beep()  # Optional: Beep to alert locally

        return img

    def capture_and_process(self, cap, model, classNames):
        while self.flag:
            success, img = cap.read()

            if not success:
                print("Failed to read frame. Exiting...")
                break

            # Process frame in a separate thread to speed up detection
            thread = threading.Thread(target=self.process_frame, args=(model, classNames, img))
            thread.start()
            thread.join()

            cv2.imshow("Image", img)

            if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
                break

    def startDetection(self, videoId):
        # Reduce frame size to 640x480
        frame_width = 640
        frame_height = 480

        if self.filename != "":
            cap = cv2.VideoCapture(self.filename)
        else:
            cap = cv2.VideoCapture(videoId)  # for webcam

        # Set the frame size
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

        model = YOLO("best.pt")
        classNames = ["fire_accident", "vehicle_accident"]

        # Start a separate thread for capturing and processing frames
        capture_thread = threading.Thread(target=self.capture_and_process, args=(cap, model, classNames))
        capture_thread.start()

        # Wait for the capture thread to finish
        capture_thread.join()

        self.filename = ""
        cap.release()
        cv2.destroyAllWindows()
    # to define detection funtionality
    # def startDetection(self, videoId):
    #
    #     if self.filename != "":
    #         cap = cv2.VideoCapture(self.filename)
    #
    #     else:
    #         cap = cv2.VideoCapture(videoId)  # for webcam
    #         cap.set(3, 1280)
    #         cap.set(4, 720)
    #
    #     model = YOLO("best.pt")
    #     classNames = ["fire_accident", "vehicle_accident"]
    #
    #     while self.flag:
    #         success, img = cap.read()
    #
    #         if not success:
    #             print("Failed to read frame. Exiting...")
    #             break
    #
    #         results = model(img, conf=0.6, stream=True)
    #
    #         for r in results:
    #             boxes = r.boxes
    #             for box in boxes:
    #                 # bounding box
    #                 x1, y1, x2, y2 = box.xyxy[0]
    #                 x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    #                 w, h = x2 - x1, y2 - y1
    #
    #                 # Additional check for valid dimensions
    #                 if w > 0 and h > 0:
    #                     cvzone.cornerRect(img, (x1, y1, w, h))
    #
    #                     # confidence
    #                     conf = math.ceil((box.conf[0] * 100)) / 100
    #
    #                     # class name
    #                     cls = int(box.cls[0])
    #                     cvzone.putTextRect(img, f'{classNames[cls]}:{conf}', (max(0, x1), max(35, y1)), scale=0.6,
    #                                     thickness=1, offset=3)
    #
    #                     # Check for accidents and update alert_message
    #                     if classNames[cls] in ["fire_accident", "vehicle_accident"]:
    #                         alert_message = f"Accident detected: {classNames[cls]}, Confidence: {conf}, Location: {self.location}"
    #                         self.notifications = alert_message
    #
    #                         # If an accident is detected, send alert message
    #                         if alert_message:
    #                             self.detected += 1
    #                             print(alert_message)
    #                             if classNames[cls] == "fire_accident":
    #                                 self.sendMessage(alert_message)
    #                             else:
    #                                 self.sendMessage1(alert_message)
    #                             #self.beep()  # Optional: Beep to alert locally
    #
    #         cv2.imshow("Image", img)
    #
    #         if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
    #             break
    #
    #     cap.release()
    #     cv2.destroyAllWindows()

# Double button class
class DoubleButtonWidgetCamera(QWidget):
    def __init__(self, row_index, row_data, sideBar):
        super().__init__()

        # store the row index and row data as instance in variables
        self.row_index = row_index
        self.row_data = row_data
        self.sideBar = sideBar  # Store a reference to MySideBar

        # get cam variable from tuple
        self.cam_name = self.row_data[0]
        self.cam_ipAddress = self.row_data[1]

        layout = QHBoxLayout(self)

        # create edit button
        self.edit_button = QPushButton("Edit", self)
        self.edit_button.setStyleSheet(u"QPushButton{\n"
                                       "	background-color: #456fed;\n"
                                       "	border-radius:10px;\n"
                                       "	color:black;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:checked{\n"
                                       "	\n"
                                       "	background-color: #082682;\n"
                                       "}")
        self.edit_button.setFixedSize(40, 25)
        self.edit_button.clicked.connect(self.edit_clicked)

        # create delete button
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setStyleSheet(u"QPushButton{\n"
                                       "	background-color: #db2336;\n"
                                       "	border-radius:10px;\n"
                                       "	color:black;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:checked{\n"
                                       "	\n"
                                       "	background-color: #9c0313;\n"
                                       "}")
        self.delete_button.setFixedSize(40, 25)
        self.delete_button.clicked.connect(self.delete_clicked)

        # live button for live footage of cam
        self.live_button = QPushButton("Live", self)
        self.live_button.setStyleSheet(u"QPushButton{\n"
                                         "	background-color: #3ef07f;\n"
                                         "	border-radius:10px;\n"
                                         "	color:black;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:checked{\n"
                                         "	\n"
                                         "	background-color:#067d32;\n" 
                                         "}")
        self.live_button.setFixedSize(40, 25)
        self.live_button.clicked.connect(self.live_clicked)

        # stop cam buttom
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setStyleSheet(u"QPushButton{\n"
                                       "	background-color: #752abf;\n"
                                       "	border-radius:10px;\n"
                                       "	color:black;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:checked{\n"
                                       "	\n"
                                       "	background-color: #752abf;\n"
                                       "}")
        self.stop_button.setFixedSize(40, 25)
        self.stop_button.clicked.connect(self.stop_clicked)

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.live_button)
        layout.addWidget(self.stop_button)

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

    def edit_clicked(self):

        # create an instance of updateCameraDialog
        self.update_dialog = updateDialog(self.row_index, self.row_data)

        # conncet the custom signal to reload cam info
        self.update_dialog.data_updated.connect(self.sideBar.reload_camList_table)

        #exceute the dialog
        self.update_dialog.exec()


    def delete_clicked(self):

        cursor = self.create_connection().cursor()

        # create a confirmation dialog
        message = QMessageBox.question(self, 'Confirmation', 'Are you sure, you want to delete'+self.cam_name+'?', QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)

        if message == QMessageBox.StandardButton.Yes:
            # delete row from the table

            delete_query = "DELETE FROM camList WHERE name=%s"
            cursor.execute(delete_query, (self.cam_name,))
            self.mydb.commit()
            self.mydb.close()

            # emit a signal to inform about data change
            self.sideBar.reload_camList_table()

    global location
    def live_clicked(self):

        cursor = self.create_connection().cursor()

        id_query = "SELECT ipAddress FROM camList WHERE name = %s"
        cursor.execute(id_query, (self.cam_name,))
        videoId = cursor.fetchone()

        location_query = "SELECT location FROM camList WHERE name = %s"
        cursor.execute(location_query, (self.cam_name,))
        self.sideBar.location = cursor.fetchone()

        self.mydb.close()
        self.sideBar.startDetection(videoId[0])

    global flag
    def stop_clicked(self):

        self.sideBar.flag = False
        cv2.destroyAllWindows()



