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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from time import sleep

from osu2 import Osuu
from cats import Cat
from loading import Loading
from xo_game import XO_game

class BBZ2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def get_windows(self, list_of_window5):
        self.list_of_window5 = list_of_window5

    def initUI(self):
        self.main_window = QWidget(self)
        self.main_window.resize(1000, 700)


        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap('./BBZ 2.0/menu_texture/menu_bg.png'))

        self.back_btn = QPushButton(self)
        self.back_btn.move(0, 325)
        self.back_btn.resize(50, 50)
        self.back_btn.setIcon(QIcon('./BBZ 2.0/menu_texture/back.png'))
        self.back_btn.setIconSize(QSize(50, 50))
        self.back_btn.clicked.connect(self.back)

    def back(self):
        self.list_of_window5.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())