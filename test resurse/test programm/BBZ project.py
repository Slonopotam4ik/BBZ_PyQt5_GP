import sys

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
from time import sleep
from osu import Osuu


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.main_window = QWidget()
        self.main_window.resize(1000, 700)
        self.main_window.setGeometry(300, 300, 1000, 700)
        self.main_window.setFixedSize(1000, 700)




        self.fon = QLabel(self)
        fon1 = QPixmap('fon.png')
        self.fon.setPixmap(fon1)
        self.fon.move(0, 0)

        self.logoThoto = QLabel(self)
        logo = QPixmap('logo1.png')
        self.logoThoto.setPixmap(logo)
        self.logoThoto.move(30, -30)

        # self.setStyleSheet("background-color: #7fc7ff")

        self.logo_bbz = QLabel(self)
        self.logo_bbz.move(400, 65)
        self.logo_bbz.setText('<b>BBZ</b>')
        app.setStyleSheet("QLabel{font-size: 80pt;}")

        self.xo_btn = QPushButton('', self)
        self.xo_btn.resize(100, 100)
        self.xo_btn.move(150, 300)
        self.xo_btn.setIcon(QIcon('xo_logo.png'))
        self.xo_btn.setIconSize(QSize(95, 95))

        self.xo_rools = QPushButton('Правила', self)
        self.xo_rools.resize(100, 50)
        self.xo_rools.move(150, 420)

        self.osu_btn = QPushButton('', self)
        self.osu_btn.resize(100, 100)
        self.osu_btn.move(350, 300)
        self.osu_btn.setIcon(QIcon('osu_logo.png'))
        self.osu_btn.setIconSize(QSize(95, 95))
        self.osu_btn.clicked.connect(self.osu_game)

        self.osu_rools = QPushButton('Правила', self)
        self.osu_rools.resize(100, 50)
        self.osu_rools.move(350, 420)

        self.goroda_btn = QPushButton('', self)
        self.goroda_btn.resize(100, 100)
        self.goroda_btn.move(550, 300)
        self.goroda_btn.setIcon(QIcon('goroda_logo'))
        self.goroda_btn.setIconSize(QSize(95, 95))

        self.goroda_rools = QPushButton('Правила', self)
        self.goroda_rools.resize(100, 50)
        self.goroda_rools.move(550, 420)

        self.cats_btn = QPushButton('', self)
        self.cats_btn.resize(100, 100)
        self.cats_btn.move(750, 300)
        self.cats_btn.setIcon(QIcon('cats_logo'))
        self.cats_btn.setIconSize(QSize(95, 95))

        self.cats_rools = QPushButton('Правила', self)
        self.cats_rools.resize(100, 50)
        self.cats_rools.move(750, 420)

        self.exit_btn = QPushButton('', self)
        self.exit_btn.resize(100, 50)
        self.exit_btn.move(0, 650)
        self.exit_btn.setIcon(QIcon('exit_button_texture.png'))
        self.exit_btn.setIconSize(QSize(100, 50))
        self.exit_btn.clicked.connect(self.exit)

        self.kalkul_btn = QPushButton('', self)
        self.kalkul_btn.resize(100, 100)
        self.kalkul_btn.move(450, 550)
        self.kalkul_btn.setIcon(QIcon('kalkul.png'))
        self.kalkul_btn.setIconSize(QSize(90, 90))

        self.crash_btn = QPushButton('', self)
        self.crash_btn.resize(50, 50)
        self.crash_btn.move(950, 650)
        self.crash_btn.setIcon(QIcon('crash.png'))
        self.crash_btn.setIconSize(QSize(90, 90))

    def osu_game(self):
        spisok_okon.setCurrentIndex(1)




        # self.hide()
        # self.osu_scene = QWidget(self, flags=Qt.Window)
        # self.osu_scene.resize(1000, 700)
        # self.osu_scene.setFixedSize(1000, 700)
        # self.osu_scene.show()
        #
        # self.osu_dificulti = QLabel(self, flags=Qt.Window)
        # self.osu_dificulti.move(50, 50)
        # self.osu_dificulti.setText('Выберите сложность: ')

    def exit(selfs):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    spisok_okon = QStackedWidget()
    smain_window = Example()
    osu_window = Osuu()

    spisok_okon.addWidget(smain_window) # 0
    spisok_okon.addWidget(osu_window) # 1

    spisok_okon.resize(1000, 700)
    spisok_okon.setFixedSize(1000, 700)
    spisok_okon.show()
    sys.exit(app.exec())
