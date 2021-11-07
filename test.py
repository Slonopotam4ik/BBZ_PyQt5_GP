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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.time = 4

        self.main_window = QWidget(self)
        self.main_window.resize(260, 200)

        self.imposible_ach = QLabel(self)
        self.imposible_ach.hide()
        self.imposible_ach.resize(260, 70)
        self.imposible_ach.setPixmap(QPixmap('./texture/achievements_texture/imposible-posible.png'))

        self.last = QLabel(self)
        self.last.hide()
        self.last.resize(260, 70)
        self.last.setPixmap(QPixmap('./texture/achievements_texture/last_chinese.png'))

        self.btn = QPushButton(self)
        self.btn.move(80, 100)
        self.btn.clicked.connect(self.imposible_achievement)

        self.btn1 = QPushButton(self)
        self.btn1.move(130, 100)
        self.btn1.clicked.connect(self.last_achievement)

    def imposible_achievement(self):
        # if not list_of_achievements[10]:
        #     list_of_achievements[10] = True
        self.imposible_ach.move(0, 0)
        self.imposible_ach.show()

        animation_curve = QEasingCurve.InQuad

        animation1 = QPropertyAnimation(self.imposible_ach, b'pos', self)
        animation1.setEasingCurve(animation_curve)
        animation1.setDuration(2000)
        animation1.setKeyValueAt(0, QPoint(-300, 0))

        self.animation2 = QPropertyAnimation(self.imposible_ach, b'pos', self)
        self.animation2.setEasingCurve(animation_curve)
        self.animation2.setDuration(2000)
        self.animation2.setKeyValueAt(0, QPoint(0, 0))

        animation1.start()
        self.imposible_achievement_timer()

    def imposible_achievement_timer(self):
        if self.time > 0:
            self.time -= 1
            QTimer().singleShot(1000, self.imposible_achievement_timer)
        else:
            self.time = 4
            self.imposible_ach.move(-300, 0)
            self.animation2.start()

    def last_achievement(self):
        # if not list_of_achievements[10]:
        #     list_of_achievements[10] = True
        self.last.move(0, 0)
        self.last.show()

        animation_curve = QEasingCurve.InQuad

        animation1 = QPropertyAnimation(self.last, b'pos', self)
        animation1.setEasingCurve(animation_curve)
        animation1.setDuration(2000)
        animation1.setKeyValueAt(0, QPoint(-300, 0))

        self.animation2_2 = QPropertyAnimation(self.last, b'pos', self)
        self.animation2_2.setEasingCurve(animation_curve)
        self.animation2_2.setDuration(2000)
        self.animation2_2.setKeyValueAt(0, QPoint(0, 0))

        animation1.start()
        self.last_achievement_timer()

    def last_achievement_timer(self):
        if self.time > 0:
            self.time -= 1
            QTimer().singleShot(1000, self.last_achievement_timer)
        else:
            self.time = 4
            self.last.move(-300, 0)
            self.animation2_2.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
