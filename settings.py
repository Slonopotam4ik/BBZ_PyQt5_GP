import os.path
import sys
from _testcapi import getbuffer_with_null_view

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QSound
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimedia import QAudioInput, QAudioFormat

# from BBZ_project import abcd

a = ''


class Setting(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def get_windows(self, list_of_window5):
        self.list_of_window5 = list_of_window5

    def initUI(self):
        self.lenguage_now = 'ru'
        self.lenguage = 'Язык'





        self.main_window = QWidget(self)
        self.main_window.resize(1000, 700)

        self.background = QLabel(self)
        self.background.resize(1000, 700)
        self.background.setPixmap(QPixmap('./texture/settings_texture/setting_background.png'))
        self.background.show()

        self.lenguage_text = QLabel(self)
        self.lenguage_text.resize(400, 100)
        self.lenguage_text.move(300, 200)
        self.lenguage_text.setText(self.lenguage)
        self.lenguage_text.setStyleSheet("QLabel{font-size: 50pt;}")

        self.language_btn = QPushButton(self)
        self.language_btn.resize(100, 100)
        self.language_btn.setIcon(QIcon('./texture/settings_texture/language_ru.png'))
        self.language_btn.setIconSize(QSize(100, 100))
        self.language_btn.move(550, 200)
        self.language_btn.clicked.connect(self.change_language_btn)

        self.exit_btn = QPushButton('<--', self)
        self.exit_btn.resize(100, 50)
        self.exit_btn.move(0, 650)
        self.exit_btn.clicked.connect(self.exit)

        self.btn_sound = QMediaPlayer()

    def play_audo_file(self):
        file = os.path.join(os.getcwd(), 'abc.mp3')
        url = QUrl.fromLocalFile(file)
        content = QMediaContent(url)
        self.btn_sound.setMedia(content)
        self.btn_sound.play()


    def change_language_btn(self):
        self.play_audo_file()
        if self.lenguage_now == 'ru':
            self.language_btn.setIcon(QIcon('./texture/settings_texture/language_en.png'))
            self.change_language_in_setting()
            change_language_in_program()
            self.lenguage_now = 'en'

        elif self.lenguage_now == 'en':
            self.language_btn.setIcon(QIcon('./texture/settings_texture/language_ru.png'))
            self.change_language_in_setting()
            change_language_in_program()
            self.lenguage_now = 'ru'


    def change_language_in_setting(self):

        if self.lenguage_now == 'ru':
            self.lenguage = 'Language'

            self.lenguage_text.setText(self.lenguage)
            self.lenguage_text.move(150, 200)
        elif self.lenguage_now == 'en':
            self.lenguage = 'Язык'
            self.lenguage_text.setText(self.lenguage)
            self.lenguage_text.move(300, 200)

    def exit(self):
        self.list_of_window5.setCurrentIndex(0)
        


            
def change_language_in_program():
    # print(text)
    if a == 'ru':
        return 'en'
    elif a == 'en':
        return 'ru'
        


# def abc():
#     print(123)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Setting()
#     ex.show()
#     sys.exit(app.exec())