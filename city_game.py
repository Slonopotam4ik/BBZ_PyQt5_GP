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
import sqlite3


class Example(QWidget):
    l_letters = 'ячсмитьбюэждлорпавыфйцукенгшщзхъё -'
    actual_letter = 'а'
    players_name = 'Авдутий'
    con = sqlite3.connect("cities.bd")
    cur = con.cursor()
    the_cities_were_said_list = []
    count_players_cities = 0


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('city_game_frame.ui', self)
        self.chat.setStyleSheet('background-color: darkgreen;')

        self.input_city.setStyleSheet("QLineEdit {background-color: rgba(0, 0, 0, 0);}")

        # self.input_city.setStyleSheet("QLineEdit { qproperty-frame: false }")
        # self.chat.setStyleSheet('background-color: darkgreen;')
        # self.chat.setStyleSheet("QLineEdit {background-color: rgba(0, 0, 0, 0);}")

        self.bg.setPixmap(QPixmap('./texture/city_game/bg.png'))
        self.exit_btn.setIcon(QIcon('./texture/city_game/exit_btn.png'))
        self.send_btn.setIcon(QIcon('./texture/city_game/enter_btn.png'))
        self.surrender_btn.setIcon(QIcon('./texture/city_game/surrender_btn.png'))
        self.leter_bg.setPixmap(QPixmap('./texture/city_game/leter_bg.png'))
        self.logo.setPixmap(QPixmap('./texture/city_game/logo.png'))


        self.bg.resize(1000, 700)
        self.exit_btn.setIconSize(QSize(160, 50))
        self.send_btn.setIconSize(QSize(170, 50))
        self.surrender_btn.setIconSize(QSize(160, 50))

        self.bg.move(0, 0)


        self.exit_btn.clicked.connect(self.exit_def)
        self.send_btn.clicked.connect(self.send_def)


    def the_city_was_said(self, city):
        return city in self.the_cities_were_said_list

    def bots_answer(self):
        list_of_cities = self.take_cities(self.actual_letter)
        selected_city = 'Я сдаюсь!'
        while not self.the_city_was_said(selected_city[0]):
            selected_city = random.choice(list_of_cities)
            self.the_cities_were_said_list.append(selected_city[0])
        self.chat.addItem('Бот: ' + selected_city[0])
        if selected_city[0][-1].lower() in 'ыьъй':
            self.actual_letter = selected_city[0][-2]
        else:
            self.actual_letter = selected_city[0][-1]




    def exit_def(self):
        pass


    def checking_for_a_string_of_letters(self, l):
        f = True
        for i in l:
            if i not in self.l_letters:
                f = False
        return f

    def take_cities(self, first_letter):

        list_of_cities = self.cur.execute("""select title from cities
    WHERE title like ? """, (first_letter.upper() + '%', )).fetchall()
        return list_of_cities


    def send_def(self):
        inputed = self.input_city.text()
        if inputed == '':
            self.input_city.setText('Напишите сюда название города на букву ' + self.actual_letter)
        elif not self.checking_for_a_string_of_letters(inputed.lower()):
            self.input_city.setText('Неправильный формат ввода')
        else:
            self.chat.addItem(self.players_name + ": " + inputed)
            gig = self.take_cities(self.actual_letter)
            if inputed[0].lower() != self.actual_letter:
                self.chat.addItem('Бот' + ": " + 'Этот город начинается не на ту букву')
            elif (inputed.title(), ) not in gig:
                self.chat.addItem('Бот' + ": " + 'Мне кажется нет такого города')
            elif inputed in self.the_cities_were_said_list:
                self.chat.addItem('Бот' + ": " + 'Мы уже использовали этот город')
            else:
                if inputed[-1].lower() in 'ыьъй':
                    self.actual_letter = inputed[-2]
                else:
                    self.actual_letter = inputed[-1]
                self.the_cities_were_said_list.append(inputed.title())
                self.count_players_cities += 1
                self.bots_answer()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
