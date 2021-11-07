from PyQt5 import uic, QtGui
import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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


class XO_game(QWidget):
    switch_counter = 0

    list_xo = [['X', '0'], ['1', '0']]
    list_colors = ["color: black", "color: #07FF00"]
    list_exit = ["./texture/xo_texture/exit_img.png", "./texture/xo_texture/exit_img_gb.png"]
    list_bg_pole = ["./texture/xo_texture/black_bg.png", "./texture/xo_texture/green_bg.png"]
    list_bg_menu = ["./texture/xo_texture/white_bg.png", "./texture/xo_texture/black_bg.png"]
    list_restart = ["./texture/xo_texture/restart_img.png", "./texture/xo_texture/restart_img_gb.png"]
    list_btn_switch = ['color: black; background-color: white; border: none',
                       'background-color: #000000; border: none; color: #07FF00']

    switcher_count = 0

    c_x = 0
    c_0 = 0

    side = 24
    length_matrix = 31
    width_matrix = 28

    x0_na_matrix = list_xo[switcher_count]
    count_x0 = 0

    otstup_x = 225
    otstup_y = 0

    spi_matrix = []
    spi_btn = []

    btn_grp = QButtonGroup()
    btn_grp.setExclusive(True)

    wins_list = [0, 0]

    def __init__(self, list_of_achievements):
        self.list_of_achievements = list_of_achievements
        super().__init__()
        self.initUI()

    def get_windows(self, list_of_window5):
        self.list_of_window5 = list_of_window5

    def initUI(self):
        uic.loadUi('./ui/x_0_frame.ui', self)

        self.setWindowIcon(QtGui.QIcon('./texture/xo_texture/icon_x_0.png'))

        self.pixmap_black = QPixmap(self.list_bg_menu[self.switcher_count])
        self.pixmap_green = QPixmap(self.list_bg_pole[self.switcher_count])

        self.black = QLabel(self)
        self.black.setPixmap(self.pixmap_black)

        self.green = QLabel(self)
        self.green.setPixmap(self.pixmap_green)

        self.green.move(self.otstup_x - 1, 0)
        self.setWindowTitle('Крестики-Нолики')

        self.turn_count = QLabel('Сейчас ходит: ' + '\n' + self.x0_na_matrix[self.count_x0], self)
        self.turn_count.setStyleSheet(self.list_colors[self.switcher_count])
        self.turn_count.setFont(QtGui.QFont("Arial", 20))

        self.count_wins = QLabel('Счёт: ' + '\n' + str(self.wins_list[0]) + ' - ' + str(self.wins_list[1]), self)
        self.count_wins.setFont(QtGui.QFont("Arial", 13))
        self.count_wins.setStyleSheet(self.list_colors[self.switcher_count])
        self.count_wins.move(50, 300)

        self.time = 4
        self.color_time = 4

        self.color_active = False
        self.is_played = False
        self.color_wait = False

        self.countX = QLabel('Количество крестиков: ' + '\n' + str(self.c_x), self)
        self.countX.setFont(QtGui.QFont("Arial", 11))
        self.countX.setStyleSheet(self.list_colors[self.switcher_count])
        self.countX.move(5, 150)
        self.countX.resize(200, 50)

        self.count0 = QLabel('Количество ноликов: ' + '\n' + str(self.c_0), self)
        self.count0.setFont(QtGui.QFont("Times", 11))
        self.count0.setStyleSheet(self.list_colors[self.switcher_count])
        self.count0.move(5, 200)
        self.count0.resize(200, 50)

        self.pole()
        self.matrix()

        self.btn_grp.buttonClicked.connect(self.najata)

        self.restart_btn = QPushButton(self)
        self.restart_btn.setIcon(QIcon(self.list_restart[self.switcher_count]))
        self.restart_btn.setIconSize(QSize(150, 40))
        self.restart_btn.resize(150, 40)
        self.restart_btn.move(35, 650)
        self.restart_btn.clicked.connect(self.restart_def)

        self.exit_btn = QPushButton(self)
        self.exit_btn.setIcon(QIcon(self.list_exit[self.switcher_count]))
        self.exit_btn.setIconSize(QSize(78, 40))
        self.exit_btn.resize(78, 40)
        self.exit_btn.move(35, 600)
        self.exit_btn.clicked.connect(self.exit_def)

        self.switch_btn = QPushButton(self)
        self.switch_btn.setIcon(QIcon("./texture/xo_texture/change_img.png"))
        self.switch_btn.setIconSize(QSize(40, 40))
        self.switch_btn.resize(40, 40)
        self.switch_btn.move(130, 600)
        self.switch_btn.clicked.connect(self.change_def)

        self.winner = QLabel('Победили: ' + '\n' + self.x0_na_matrix[(self.switcher_count + 1) % 2], self)
        self.winner.setFont(QtGui.QFont("Times", 13))
        self.winner.setStyleSheet(self.list_colors[self.switcher_count])
        self.winner.move(10, 70)
        self.winner.resize(100, 100)
        self.winner.hide()

        self.xo_achievement = QLabel(self)
        self.xo_achievement.resize(260, 70)
        self.xo_achievement.setPixmap(QPixmap('./texture/achievements_texture/xo.png'))
        self.xo_achievement.hide()

        self.color_achievement = QLabel(self)
        self.color_achievement.resize(260, 70)
        self.color_achievement.setPixmap(QPixmap('./texture/achievements_texture/color_soul.png'))
        self.color_achievement.hide()

    def change_def(self):
        self.switcher_count = (self.switcher_count + 1) % 2
        self.x0_na_matrix = self.list_xo[self.switcher_count]

        for i in range(self.width_matrix):
            for j in range(self.length_matrix):
                self.spi_btn[i][j].setStyleSheet(self.list_btn_switch[self.switcher_count])
                if self.spi_matrix[i][j] in self.list_xo[(self.switcher_count + 1) % 2]:
                    self.spi_btn[i][j].setText(
                        self.x0_na_matrix[self.list_xo[(self.switcher_count + 1) % 2].index(self.spi_matrix[i][j])])
                    self.spi_matrix[i][j] = self.x0_na_matrix[
                        self.list_xo[(self.switcher_count + 1) % 2].index(self.spi_matrix[i][j])]

        self.turn_count.setText('Сейчас ходит: ' + '\n' + self.x0_na_matrix[self.count_x0])

        self.countX.setStyleSheet(self.list_colors[self.switcher_count])
        self.count0.setStyleSheet(self.list_colors[self.switcher_count])

        self.restart_btn.setIcon(QIcon(self.list_restart[self.switcher_count]))
        self.exit_btn.setIcon(QIcon(self.list_exit[self.switcher_count]))

        self.pixmap_green = QPixmap(self.list_bg_pole[self.switcher_count])
        self.pixmap_black = QPixmap(self.list_bg_menu[self.switcher_count])

        self.count_wins.setStyleSheet(self.list_colors[self.switcher_count])
        self.turn_count.setStyleSheet(self.list_colors[self.switcher_count])

        self.black.setPixmap(self.pixmap_black)
        self.green.setPixmap(self.pixmap_green)

        self.switch_counter += 1
        if (self.switch_counter == 10) and (self.list_of_achievements[7] == False):
            self.achivement_change()

        self.winner.setStyleSheet(self.list_colors[self.switcher_count])
        self.winner.setText('Победили: ' + '\n' + self.spi_matrix[0][0])

    def achivement_change(self):
        self.list_of_achievements[7] = True
        self.color_animation()

    def xo_animation(self):
        if self.color_active:
            self.xo_achievement.move(0, 75)
        else:
            self.xo_achievement.move(0, 0)
        self.xo_achievement.show()

        animation_curve = QEasingCurve.InQuad

        animation1 = QPropertyAnimation(self.xo_achievement, b'pos', self)
        animation1.setEasingCurve(animation_curve)
        animation1.setDuration(2000)
        if self.color_active:
            animation1.setKeyValueAt(0, QPoint(-300, 75))
        else:
            animation1.setKeyValueAt(0, QPoint(-300, 0))

        self.animation3 = QPropertyAnimation(self.xo_achievement, b'pos', self)
        self.animation3.setEasingCurve(animation_curve)
        self.animation3.setDuration(2000)
        if self.color_active:
            self.animation3.setKeyValueAt(0, QPoint(0, 75))
        else:
            self.animation3.setKeyValueAt(0, QPoint(0, 0))

        animation1.start()
        self.xo_animation_timer()

    def xo_animation_timer(self):
        if self.time > 0:
            self.time -= 1
            QTimer().singleShot(1000, self.xo_animation_timer)
        else:
            self.time = 4
            if self.color_active:
                self.xo_achievement.move(-300, 75)
            else:
                self.xo_achievement.move(-300, 0)
            self.animation3.start()

    def color_animation(self):
        self.color_active = True
        self.color_achievement.move(0, 0)
        self.color_achievement.show()

        animation_curve = QEasingCurve.InQuad

        animation1 = QPropertyAnimation(self.color_achievement, b'pos', self)
        animation1.setEasingCurve(animation_curve)
        animation1.setDuration(2000)
        animation1.setKeyValueAt(0, QPoint(-300, 0))

        self.animation3_1 = QPropertyAnimation(self.color_achievement, b'pos', self)
        self.animation3_1.setEasingCurve(animation_curve)
        self.animation3_1.setDuration(2000)
        self.animation3_1.setKeyValueAt(0, QPoint(0, 0))

        animation1.start()
        self.color_animation_timer()

    def color_animation_timer(self):
        if self.color_time > 0:
            self.color_time -= 1
            QTimer().singleShot(1000, self.color_animation_timer)
        else:
            self.color_time = 4
            self.color_achievement.move(-300, 0)
            self.animation3_1.start()

    def restart_def(self):
        for i in range(self.width_matrix):
            for j in range(self.length_matrix):
                self.spi_btn[i][j].setText('')
                self.spi_btn[i][j].setEnabled(True)

        for i in range(self.width_matrix):
            for j in range(self.length_matrix):
                self.spi_matrix[i][j] = 'N'

        self.c_0 = 0
        self.c_x = 0

        self.count_x0 = 0
        self.countX.setText('Количество крестиков: ' + '\n' + str(self.c_x))
        self.count0.setText('Количество ноликов: ' + '\n' + str(self.c_0))
        self.turn_count.setText('Сейчас ходит: ' + '\n' + self.x0_na_matrix[self.count_x0])

        self.winner.hide()

    def matrix(self):
        self.spi_matrix = []
        for i in range(self.width_matrix):
            k = []
            self.spi_matrix.append(k)
            for j in range(self.length_matrix):
                self.spi_matrix[i].append('N')

    def najata(self, btn):
        if self.is_played == False:
            self.list_of_achievements[6] = True
            self.xo_animation()
            self.is_played = True
        f = False

        for i in self.spi_btn:
            if btn in i and self.spi_matrix[self.spi_btn.index(i)][i.index(btn)] == 'N':
                self.spi_matrix[self.spi_btn.index(i)][i.index(btn)] = self.x0_na_matrix[self.count_x0]
                f = True
                y = self.spi_btn.index(i)
                x = i.index(btn)
                break

        if f:
            btn.setText(self.x0_na_matrix[self.count_x0])
            self.grinch = self.x0_na_matrix[self.count_x0]

            if self.count_x0 % 2 == 0:
                self.c_x += 1
                self.countX.setText('Количество крестиков: ' + '\n' + str(self.c_x))
            else:
                self.c_0 += 1
                self.count0.setText('Количество ноликов: ' + '\n' + str(self.c_0))
            if self.proverka_pobedi(x, y):
                self.wins_list[self.count_x0] += 1
                self.count_wins.setText('Счёт: ' + '\n' + str(self.wins_list[0]) + ' - ' + str(self.wins_list[1]))
                self.win()

            self.count_x0 = (self.count_x0 + 1) % 2
            self.turn_count.setText('Сейчас ходит: ' + '\n' + self.x0_na_matrix[self.count_x0])

    def win(self):
        for i in range(self.width_matrix):
            for j in range(self.length_matrix):
                self.spi_btn[i][j].setText(self.x0_na_matrix[self.count_x0])
                self.spi_btn[i][j].setEnabled(False)
                self.spi_matrix[i][j] = self.x0_na_matrix[self.count_x0]

        self.winner.setText('Победили: ' + '\n' + self.grinch)
        self.winner.show()

    def pole(self):
        for i in range(self.width_matrix):
            self.spi_btn.append([])
            for j in range(self.length_matrix):
                k = QPushButton('', self)
                k.setFont(QtGui.QFont("Arial", 16))
                k.resize(self.side, self.side)
                k.setStyleSheet(self.list_btn_switch[self.switcher_count])
                k.move(j * self.side + self.otstup_x + j, self.side * i + self.otstup_y + i)

                self.btn_grp.addButton(k)
                self.spi_btn[i].append(k)

    def proverka_pobedi(self, x, y):
        length = self.length_matrix
        width = self.width_matrix

        spi_gorizont = self.spi_matrix[y][min(abs(x - 4), abs(x - 3), abs(x - 2), abs(x - 1), x): x + 5]
        if self.x0_na_matrix[self.count_x0] * 5 in ''.join(spi_gorizont):
            return True

        spi_vertical = []
        spi_of_spi = self.spi_matrix[min(abs(y - 4), abs(y - 3), abs(y - 2), abs(y - 1), y): y + 5]
        for i in spi_of_spi:
            spi_vertical.append(i[x])
        if self.x0_na_matrix[self.count_x0] * 5 in ''.join(spi_vertical):
            return True

        spi_diagonal1 = []
        for i in range(- 4, 5):
            if not (x + i < 0 or y + i < 0 or y + i > width - 1 or x + i > length - 1):
                spi_diagonal1.append(self.spi_matrix[y + i][x + i])

        if self.x0_na_matrix[self.count_x0] * 5 in ''.join(spi_diagonal1):
            return True

        spi_diagonal2 = []
        for i in range(-4, 5):
            if not (x + i < 0 or y - i < 0 or y - i > width - 1 or x + i > length - 1):
                spi_diagonal2.append(self.spi_matrix[y - i][x + i])

        if self.x0_na_matrix[self.count_x0] * 5 in ''.join(spi_diagonal2):
            return True

    def exit_def(self):
        self.list_of_window5.setCurrentIndex(0)
