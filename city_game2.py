from PyQt5 import uic, QtGui
import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
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
import sqlite3


class City_game(QWidget):
    special_gnom = False
    l_letters = 'ячсмитьбюэждлорпавыфйцукенгшщзхъё -'  # разрешённые буквы для ввода названия города
    actual_letter = 'а'  # Буква, на которую нужно назвать город
    players_name = ''  # Имя игрока
    con = sqlite3.connect("./bd/cities.bd")  # подключение к БД
    cur = con.cursor()
    the_cities_were_said_list = ['лол']  # список городов, которых уже называли
    count_players_cities = 49  # Количество правильно сказанных городов, которых сказал игрок
    hi_name = ['Добро пожаловать в игру, ', 'Привет, ', 'Хай, ', 'Здравствуй, ']  # Список приветствий для игрока
    wrong_city = ['Позвольте, мне кажется, такого города не существует', 'Такого города нет', 'Это что за новый город?',
                  'Красивое название несуществующего города',
                  'Вы ошиблись']  # Список ответов, если игрок введет неправильное название города
    wrong_letter = ['Но я вам загадывал другую букву', 'Этот город начинается не на ту букву',
                    'Вы меня не обманите']  # Список ответов, если игрок введет город не на ту букву
    city_used = ['Очень странно...Где-то я это уже слышал', 'Мы этот город уже называли',
                 'Кто-то из нас уже называл этот город']
    # Список ответов, если игрок введет город, который уже называли
    bots_answer = [hi_name, wrong_city, wrong_letter, city_used]

    def __init__(self, list_of_achievements):
        self.list_of_achievements = list_of_achievements
        super().__init__()
        self.initUI()

    def get_windows(self, list_of_window5):
        self.list_of_window5 = list_of_window5

    def initUI(self):
        uic.loadUi('./ui/city_game_frame2.ui', self)

        self.chat.setStyleSheet('background-color: darkgreen;')
        # self.input_city.setStyleSheet("QLineEdit {background-color: rgba(0, 0, 0, 0);}")
        self.input_city.setStyleSheet('background-color: darkgreen;')

        self.bg.setPixmap(QPixmap('./texture/city_game/bg.png'))
        self.exit_btn.setIcon(QIcon('./texture/city_game/exit_btn.png'))
        self.send_btn.setIcon(QIcon('./texture/city_game/enter_btn.png'))
        self.surrender_btn.setIcon(QIcon('./texture/city_game/surrender_btn.png'))
        self.words_cities.setPixmap(QPixmap('./texture/city_game/leter_bg.png'))
        self.logo.setPixmap(QPixmap('./texture/city_game/logo.png'))
        self.yes_btn.setIcon(QIcon('./texture/city_game/yes_bnt.png'))

        self.bg.resize(1000, 700)
        self.exit_btn.setIconSize(QSize(100, 60))
        self.send_btn.setIconSize(QSize(160, 60))
        self.surrender_btn.setIconSize(QSize(120, 60))
        self.yes_btn.setIconSize(QSize(100, 60))

        self.bg.move(0, 0)
        self.words_cities.show()

        # self.chat.moveCursor(QtGui.QTextCursor.End)
        # self.chat.ensureCursorVisible()

        self.exit_btn.clicked.connect(self.exit)  # вызывает функцию exit_def при нажатии на кнопку выхода
        self.send_btn.clicked.connect(self.send_def)  # вызывает функцию send_def при нажатии на кнопку отправки
        # self.clear_btn.clicked.connect(self.clear_input_def)
        # вызывает функцию clear_input_def при нажатии на кнопку очистки
        self.surrender_btn.clicked.connect(self.surrender_def)
        # вызывает функцию surrender_def при нажатии на кнопку "Сдаться"
        self.input_ur_name()
        # Функция, отвечающая за принятие имени игрока
        self.words_cities.setText(self.words_cities.text() + self.actual_letter.upper())
        self.words_cities.move(145, 5)
        # создание надписи "количество городов на данную букву"
        self.number_of_cities.setText(str(len(self.take_cities(self.actual_letter))))
        # создание и показ кол-ва городов на данную букву
        # (он отправляет в функцию take_cities запрос на получение списка
        # городов наинающихся с actual_letter и ищет количество элементов этого списка)
        self.yes_btn.clicked.connect(self.input_ur_name)
        # вызывает функцию input_ur_name при нажатии на кнопку Yes в конце игры

        self.imposible_ach = QLabel(self)
        self.imposible_ach.resize(260, 70)
        self.imposible_ach.move(-300, 0)
        self.imposible_ach.setPixmap(QPixmap('./texture/achievements_texture/imposible-posible.png'))
        self.imposible_ach.hide()

        self.last = QLabel(self)
        self.last.show()
        self.last.hide()
        self.last.resize(260, 70)
        self.last.setPixmap(QPixmap('./texture/achievements_texture/last_chinese.png'))

        self.time = 4
        self.time1 = 4

        self.count_of_lying = 0

    def clear_input_def(self):
        self.input_city.setText('')  # Очищает поля для ввода

    def input_ur_name(self):
        # делает все кнопки активными для нажатия, поле для ввода активным для ввода, запрашивает и принимает имя игрока
        self.the_cities_were_said_list = []
        self.count_players_cities = 48
        self.chat.clear()
        self.number_of_cities.hide()
        self.words_cities.hide()
        self.input_city.setReadOnly(False)
        self.surrender_btn.setEnabled(True)
        self.send_btn.setEnabled(True)
        # self.clear_btn.setEnabled(True)
        self.exit_btn.setEnabled(True)
        self.chat.addItem('Бот: Введите ваше имя (не более 16 символов)')
        self.special_gnom = True
        self.yes_btn.hide()

    def surrender_def(self):
        # делает все кнопки неактивными для нажатия, поле для ввода неактивным для ввода, благодарит за игру и
        # показывает счёт, если число очков заканчивается на 1 2 3 4, то в конце пишет очка, иначе очков,
        # вызывает функцию do_u_want_again
        self.input_city.setReadOnly(True)
        self.surrender_btn.setEnabled(False)
        self.send_btn.setEnabled(False)
        # self.clear_btn.setEnabled(False)
        if self.count_players_cities % 10 > 0 and self.count_players_cities % 10 < 5:
            self.chat.addItem('Бот: Вы набрали ' + str(self.count_players_cities) + ' очка')
        else:
            self.chat.addItem('Бот: Вы набрали ' + str(self.count_players_cities) + ' очков')
        self.chat.addItem('Бот: Спасибо за игру')
        self.input_city.setText('')  # очищает поле для ввода
        self.do_u_want_again()

    def u_won(self):
        # делает все кнопки неактивными для нажатия, поле для ввода неактивным для ввода, говорит, что игрок победил,
        # благодарит за игру и показывает счёт, если число очков заканчивается на 1 2 3 4,
        # то в конце пишет очка, иначе очков, вызывает функцию do_u_want_again
        self.chat.addItem('Бот' + ": " + 'Вы победили')
        if self.count_players_cities % 10 > 0 and self.count_players_cities % 10 < 5:
            self.chat.addItem('Бот: Вы набрали ' + str(self.count_players_cities) + ' очка')
        else:
            self.chat.addItem('Бот: Вы набрали ' + str(self.count_players_cities) + ' очков')
        self.chat.addItem('Бот: Спасибо за игру')
        self.input_city.setReadOnly(True)
        self.surrender_btn.setEnabled(False)
        self.send_btn.setEnabled(False)
        self.clear_btn.setEnabled(False)
        print(self.players_name + ' == ' + str(self.count_players_cities))
        self.input_city.setText('')  # очищает поле для ввода
        self.do_u_want_again()

    def do_u_want_again(self):
        # оказывает кнопку Yes, задаёт вопрос 'Хотите начать сначала?'
        self.chat.addItem('Бот' + ": " + 'Хотите начать сначала?')
        self.yes_btn.show()

    def the_city_was_said(self, city):
        # получает на вход название города, на выход отдаёт True либо False,
        # в зависимости находится город в списке the_cities_were_said_list или нет
        return city in self.the_cities_were_said_list

    def bots_answer(self):
        list_of_cities = self.take_cities(self.actual_letter)
        # с помощью функции take_cities получает список городов с именемна букву actual_letter
        selected_city = self.the_cities_were_said_list
        # создание строки названия выбранного города
        if self.check_this_list(self.take_cities(self.actual_letter)) > 5:
            # если количество городов которых нет в списке the_cities_were_said_list,
            # начинающихся с буквы actual_letter больше пяти, то выполнить основную программу,
            # иначе вызвать функцию u_won()
            while self.the_city_was_said(selected_city[0]):
                # пока первыый элемент кортежа the_city_was_said находится в списке the_cities_were_said_list,
                # присваивает переменной selected_city случайный элемент из кортежа list_of_cities
                selected_city = random.choice(list_of_cities)

            self.the_cities_were_said_list.append(selected_city[0])
            # добавление выбранного города в список the_city_was_said
            self.chat.addItem('Бот: ' + selected_city[0])  # Бот пишет в чат выбранный город
            if selected_city[0][-1].lower() in 'ыьъй':
                # если на конце выбранного города буква 'ы', 'ъ', 'ь', или 'й',
                # то буква на которую должен сказать город игрок будет предпоследней
                self.actual_letter = selected_city[0][-2]
            else:
                self.actual_letter = selected_city[0][-1]
            self.words_cities.setText(self.words_cities.text()[:-1] + self.actual_letter.upper())
            # Замена буквы на конце на актуальную
            self.number_of_cities.setText(str(self.check_this_list(self.take_cities(self.actual_letter))))
            # показ кол-ва городов на данную букву
        else:
            self.u_won()

    def check_this_list(self, list_k):
        # На вход список городов, на выход количество городов, которых нет в списке "использованных"
        k = 0
        for i in list_k:
            if i[0] not in self.the_cities_were_said_list:
                k += 1
        return k

    def checking_for_a_string_of_letters(self, l):
        # Функция проверки строки на непридвиденные символы, если в строке есть символ,
        # которого нет в списке "придвиденных символов", то на выход подается False иначе True
        f = True
        for i in l:
            if i not in self.l_letters:
                f = False
        return f

    def take_cities(self, first_letter):
        # Функция принимает на вход букву и выводит список названий городов, которые начинаются на данную букву

        list_of_cities = self.cur.execute("""select title from cities
    WHERE title like ? """, (first_letter.upper() + '%',)).fetchall()
        return list_of_cities

    def send_def(self):
        inputed = self.input_city.text()
        # В переменную inputed записывается данные, полученные с поля ввода
        if self.special_gnom:
            # если кнопку ввода нажал игрок сразу после выполнения функции input_ur_name,
            # то inputed записывается уже в переменную имени игрока
            if inputed == '' or len(inputed) > 16:
                # если на вход пустая строка, или символов в строке больше 16, то написать о том,
                # что неправильный формат ввода
                self.input_city.setText('Неправильный формат ввода')
            else:
                self.players_name = inputed
                self.chat.addItem('Бот: ' + random.choice(self.hi_name) + self.players_name)
                # случайно выбирает фразу приветствия
                self.chat.addItem('Бот: ' + 'Назовите город на букву А')  # говорит на какую букву нужно назвать город
                self.special_gnom = False  # "открывает дверь" в основную программу
                self.number_of_cities.show()  # показывает количество городов на данную букву
                self.words_cities.show()
                self.input_city.setText('')  # очищает поле для ввода
        elif inputed == '':
            self.input_city.setText('Введите города на букву ' + self.actual_letter)
            # если строка пустая, то объясняет игроку, что надо сделать
        elif not self.checking_for_a_string_of_letters(inputed.lower()):
            self.input_city.setText('Неправильный формат ввода')
            self.input_city.setText('')  # очищает поле для ввода
            # если игрок ввёл неправильные символы, говорит об этом игроку
        else:  # если всё с форматом данных правильно, то он проверяет дальше
            self.chat.addItem(self.players_name + ": " + inputed)  # добавляет сообщение игрока в чат
            gig = self.take_cities(self.actual_letter)
            # я забыл как расшифровывается гиг, но я туда записываю список возможных городов на данную букву
            if inputed[0].lower() != self.actual_letter:
                # если Первая БуКвА названия города неправильная,
                # то бот говорит об этом игроку случайно выбранной фразой об этом
                self.chat.addItem('Бот' + ": " + random.choice(self.wrong_letter))
                self.input_city.setText('')  # очищает поле для ввода
                self.count_of_lying += 1
                self.lying()
            elif (inputed.title(),) not in gig:
                # если в БД нет такого города, то бот говорит об этом игроку случайно выбранной фразой об этом
                self.chat.addItem('Бот' + ": " + random.choice(self.wrong_city))
                self.input_city.setText('')  # очищает поле для ввода
                self.count_of_lying += 1
                self.lying()
            elif inputed in self.the_cities_were_said_list:
                # если город уже называли, то бот говорит об этом игроку случайно выбранной фразой об этом
                self.chat.addItem('Бот' + ": " + random.choice(self.city_used))
                self.input_city.setText('')  # очищает поле для ввода
                self.count_of_lying += 1
                self.lying()
            else:  # если всё хорошо, то заканчивает проверку
                if inputed[-1].lower() in 'ыьъй':
                    # если на конце выбранного города буква 'ы', 'ъ', 'ь', или 'й',
                    # то буква на которую должен сказать город бот будет предпоследней
                    self.actual_letter = inputed[-2]
                else:
                    self.actual_letter = inputed[-1]
                self.the_cities_were_said_list.append(inputed.title())
                # добавляет в список использованных городов город, который назвал игрок
                self.count_players_cities += 1  # добавляет одно очко в счёт игрока
                self.count.setText(str(self.count_players_cities))
                if (self.count_players_cities == 50) and (not self.list_of_achievements[8]):
                    self.imposible_achievement()
                    self.list_of_achievements[8] = True
                self.input_city.setText('')  # очищает поле для ввода
                self.bots_answer()  # запускает функцию ответа бота

    def lying(self):
        if (self.count_of_lying == 5) and (not self.list_of_achievements[9]):
            self.last_achievement()
            self.list_of_achievements[9] = True

    def imposible_achievement(self):
        self.imposible_ach.hide()
        self.imposible_ach.move(0, 0)

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
        self.imposible_ach.show()
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

    def exit(self):
        self.exit_def()

    def exit_def(self):  # Функция выхода в главное меню
        self.the_cities_were_said_list = []
        self.count_players_cities = 0
        self.chat.clear()
        self.input_city.setText('')  # очищает поле для ввода
        self.number_of_cities.hide()
        self.words_cities.hide()
        self.input_city.setReadOnly(False)
        self.surrender_btn.setEnabled(True)
        self.send_btn.setEnabled(True)
        # self.clear_btn.setEnabled(True)
        self.exit_btn.setEnabled(True)
        self.chat.addItem('Бот: Введите ваше имя (не более 16 символов)')
        self.special_gnom = True
        self.yes_btn.hide()
        self.list_of_window5.setCurrentIndex(0)
