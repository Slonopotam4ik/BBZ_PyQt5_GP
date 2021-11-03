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

from PyQt5.QtWidgets import QApplication, QWidget


class Loading(QWidget):
    def get_windows(self, list_of_window3):
        self.list_of_window3 = list_of_window3

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.leter_B1_pos_x = -80
        self.leter_B1_pos_y = 300

        self.leter_B2_pos_x = 480
        self.leter_B2_pos_y = 0

        self.leter_Z_pos_x = 1050
        self.leter_Z_pos_y = 300

        self.loading_btn_size_x = 20
        self.loading_btn_size_y = 15

        self.timer = 2

        self.main_window = QWidget()
        self.main_window.resize(1000, 700)
        self.main_window.setWindowTitle('BBZ_game')
        # self.main_window.setGeometry(300, 300, 1000, 700)
        self.main_window.setFixedSize(1000, 700)
        self.main_window.setWindowOpacity(0.5)
        # self.loading_background.move(0, 0)

        self.text = QLabel(self)
        politick = open('politic.txt', encoding='utf-8').read().split('\n')
        for i in politick:
            self.text.setText(self.text.text() + i + '\n')

        self.scroll_area = QScrollArea()
        self.scroll_area.setWindowTitle("Политика конфидециальности")

        self.scroll_area.setFixedSize(400, 500)
        self.scroll_area.setWidget(self.text)

        self.scroll_area.hide()

        self.background = QLabel(self)
        self.background.resize(1000, 700)
        self.background.setFixedSize(1000, 700)
        self.background.setPixmap(QPixmap('./texture/loading_texture/loading_background.png'))

        self.politic_background = QLabel(self)
        self.politic_background.resize(1000, 700)
        self.politic_background.setFixedSize(1000, 700)
        self.politic_background.setPixmap(QPixmap('./texture/loading_texture/politic_background.png'))
        self.politic_background.hide()

        self.progess_bar = QLabel(self)
        self.progess_bar.move(264, 464)
        self.progess_bar.resize(570, 26)
        self.progess_bar.setPixmap(QPixmap('./texture/loading_texture/loading_progress_bar.png'))

        self.loading_btn = QPushButton(self)
        self.loading_btn.move(270, 470)
        self.loading_btn.resize(self.loading_btn_size_x, self.loading_btn_size_y)
        self.loading_btn.setStyleSheet('background: rgb(255, 255, 255);')
        self.loading_btn.clicked.connect(self.bonus_show)

        self.loading_btn.hide()

        self.later_B1 = QLabel(self)
        self.later_B1.move(380, 300)
        self.later_B1.setPixmap(QPixmap('./texture/loading_texture/later_B1.png'))
        self.later_B1.setPalette(self.palette())
        self.later_B1.setWindowOpacity(1 - 5)

        self.later_B2 = QLabel(self)
        self.later_B2.move(self.leter_B2_pos_x, self.leter_B2_pos_y)
        self.later_B2.setPixmap(QPixmap('./texture/loading_texture/later_B2.png'))
        self.later_B2.show()

        self.later_Z = QLabel(self)
        self.later_Z.move(self.leter_Z_pos_x, self.leter_Z_pos_y)
        self.later_Z.setPixmap(QPixmap('./texture/loading_texture/later_Z.png'))
        self.later_Z.show()

        self.bonus = QLabel(self)
        self.bonus.resize(150, 70)
        self.bonus.move(300, 500)
        self.bonus.setPixmap(QPixmap('./texture/loading_texture/bonus.png'))
        self.bonus.hide()

        self.politic_btn = QPushButton(self)
        self.politic_btn.setIcon(QIcon('./texture/loading_texture/here_texture'))
        self.politic_btn.setIconSize(QSize(100, 50))
        self.politic_btn.resize(70, 50)
        self.politic_btn.move(870, 497)
        self.politic_btn.hide()
        self.politic_btn.clicked.connect(self.privat_policy)

        self.politic_accept_btn = QPushButton('Принять', self)
        self.politic_accept_btn.setIconSize(QSize(100, 50))
        self.politic_accept_btn.resize(100, 50)
        self.politic_accept_btn.move(380, 550)
        self.politic_accept_btn.hide()
        self.politic_accept_btn.clicked.connect(self.start)

        self.politic_not_accept_btn = QPushButton('Отклонить', self)
        self.politic_not_accept_btn.setIconSize(QSize(100, 50))
        self.politic_not_accept_btn.resize(100, 50)
        self.politic_not_accept_btn.move(500, 550)
        self.politic_not_accept_btn.hide()
        self.politic_not_accept_btn.clicked.connect(self.exit_game)

        self.scip_btn = QPushButton(self)
        self.scip_btn.resize(50, 50)
        self.scip_btn.move(950, 650)
        self.scip_btn.setIcon(QIcon('./texture/loading_texture/scip_btn.png'))
        self.scip_btn.setIconSize(QSize(50, 50))
        self.scip_btn.clicked.connect(self.start)

        self.one_player_game = QPushButton(self)
        self.one_player_game.resize(200, 50)
        self.one_player_game.move(420, 400)
        self.one_player_game.setIcon(QIcon('./texture/loading_texture/one_player_btn.png'))
        self.one_player_game.setIconSize(QSize(200, 50))
        self.one_player_game.clicked.connect(self.one_player)
        self.one_player_game.hide()

        self.loading()
        self.animation()

    def bonus_show(self):
        self.bonus.show()
        self.bonus_timer()

    def bonus_timer(self):
        if self.timer > 0:
            self.timer -= 2
            QTimer().singleShot(1000, self.bonus_timer)
        else:
            self.timer = 2
            self.bonus.hide()

    def animation(self):
        animation_curve = QEasingCurve.OutBounce

        self.later_B1.move(380, 300)
        self.later_B2.move(480, 300)
        self.later_Z.move(580, 300)

        animation1 = QPropertyAnimation(self.later_B1, b'pos', self)
        animation1.setEasingCurve(animation_curve)
        animation1.setDuration(4500)
        animation1.setKeyValueAt(0, QPoint(-80, 300))

        animation2 = QPropertyAnimation(self.later_Z, b'pos', self)
        animation2.setEasingCurve(animation_curve)
        animation2.setDuration(4500)
        animation2.setKeyValueAt(0, QPoint(1050, 300))

        animation3 = QPropertyAnimation(self.later_B2, b'pos', self)
        animation3.setEasingCurve(animation_curve)
        animation3.setDuration(3500)
        animation3.setKeyValueAt(0, QPoint(480, -100))

        first_animation_group = QParallelAnimationGroup(self)
        first_animation_group.addAnimation(animation1)
        first_animation_group.addAnimation(animation2)
        first_animation_group.addAnimation(animation3)
        first_animation_group.start()

    def animation_up(self):
        animation_curve1 = QEasingCurve.InQuad

        self.later_B1.move(380, 220)
        self.later_B2.move(480, 220)
        self.later_Z.move(580, 220)

        animation1_1 = QPropertyAnimation(self.later_B1, b'pos', self)
        animation1_1.setEasingCurve(animation_curve1)
        animation1_1.setDuration(1000)
        animation1_1.setKeyValueAt(0, QPoint(380, 300))

        animation2_2 = QPropertyAnimation(self.later_Z, b'pos', self)
        animation2_2.setEasingCurve(animation_curve1)
        animation2_2.setDuration(1200)
        animation2_2.setKeyValueAt(0, QPoint(580, 300))

        animation3_3 = QPropertyAnimation(self.later_B2, b'pos', self)
        animation3_3.setEasingCurve(animation_curve1)
        animation3_3.setDuration(1100)
        animation3_3.setKeyValueAt(0, QPoint(480, 300))

        second_animation_group = QParallelAnimationGroup(self)
        second_animation_group.addAnimation(animation1_1)
        second_animation_group.addAnimation(animation2_2)
        second_animation_group.addAnimation(animation3_3)
        second_animation_group.start()

    def loading(self):
        if self.loading_btn_size_x < 495:
            self.loading_btn.show()
            self.loading_btn_size_x += 1
            self.loading_btn.resize(self.loading_btn_size_x, self.loading_btn_size_y)
            QTimer().singleShot(9.5, self.loading)
        else:
            self.bonus.hide()
            self.progess_bar.hide()
            self.politic_btn.show()
            self.loading_btn.hide()
            self.politic_background.show()

    def privat_policy(self):
        self.scroll_area.hide()
        self.scroll_area.show()
        self.politic_accept_btn.show()
        self.politic_not_accept_btn.show()

    def one_player(self):
        self.list_of_window3.setCurrentIndex(0)

    def start(self):
        self.animation_up()
        self.politic_background.hide()
        self.politic_accept_btn.hide()
        self.politic_not_accept_btn.hide()
        self.politic_btn.hide()
        self.scroll_area.close()
        self.timer = 0
        self.animation_up_timer()

    def animation_up_timer(self):
        if self.timer < 1:
            self.timer += 1
            QTimer().singleShot(1000, self.animation_up_timer)
        else:
            self.one_player_game.show()
            self.timer = 0

    def exit_game(self):
        exit()
