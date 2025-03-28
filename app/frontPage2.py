import sys

from PySide6.QtWidgets import QMainWindow, QMenu, QTableWidgetItem, QTextEdit, QFileDialog, QWidget, QMessageBox, QDialog, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from PySide6.QtGui import QAction, QIcon
from ui_index_2 import Ui_MainWindow
import requests

class MySideBar2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Strive")
        self.setWindowIcon(QIcon("strive.png"))

        # Hide widget menu
        self.icon_text_widget.setHidden(True)

        # to set default page as dashboard
        self.stackedWidget.setCurrentIndex(0)

        # connect Buttons to switch pages
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.notifications_1.clicked.connect(self.switch_to_notfications_page)
        self.notifications_2.clicked.connect(self.switch_to_notfications_page)

        self.new_1.clicked.connect(self.switch_to_news_page)
        self.news_2.clicked.connect(self.switch_to_news_page)

        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page)

        self.searchbar.textChanged.connect(self.search_page)

        self.api_key = '028d43579e5447b0a0ac7f7abe4a8604'
        self.base_url = 'https://newsapi.org/v2/top-headlines'
        self.initial_news()
        self.fetch_news()

        self.current_theme = "Light"
        self.set_theme(self.current_theme)
        self.pushButton_6.clicked.connect(self.toggle_theme)

        # methods to switch different pages
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_notfications_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_news_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(3)

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

    def search_page(self):
        text = self.searchbar.text()

        if text == "notifications":
            self.switch_to_notfications_page()
        elif text == "news":
            self.switch_to_news_page()
        elif text == "settings":
            self.switch_to_settings_page()
        else:
            self.switch_to_dashboard_page()

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