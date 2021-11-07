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
from BBZ_project_v2 import BBZ2

list_of_achievements = [False, False, False, False, False, False, False, False, True, True, False, False, False]


# list_of_achievements = [False, False, False, False, False, False, False, False, True, True, False, False, False]
# list_of_achievements = [False, True, True, True, True, True, True, True, True, True, True, False]

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.xo_rules_is_active = False
        self.osu_rules_is_active = False
        self.city_game_rules_is_active = False
        self.cats_rules_is_active = False
        self.is_active = False

        self.city_game_played = False
        self.osu_game_played = False
        self.xo_game_played = False
        self.cats_game_played = False

        self.xo_rules_count = 0
        self.osu_rules_count = 0
        self.cats_rules_count = 0
        self.city_rules_count = 0
        self.rules_count = 0

        self.timer = 3
        self.time = 4
        self.secret_time = 4
        self.end_time = 4
        self.time_bbz_ach = 4
        self.btn_time = 1

        self.mouse_x = 660
        self.mouse_y = -10
        self.mouse_an_x = 660
        self.mouse_an_y = 10
        self.bonus_mouse_wait = 1

        self.main_window = QWidget()
        self.main_window.resize(1000, 700)
        self.main_window.setGeometry(300, 300, 1000, 700)
        self.main_window.setFixedSize(1000, 700)

        self.background = QLabel(self)
        background1 = QPixmap('./texture/menu_texture/background_menu')
        self.background.setPixmap(background1)
        self.background.move(0, 0)

        # Бонус кнопки
        self.bonus1 = QLabel(self)
        self.bonus1.setPixmap(QPixmap('./texture/menu_texture/bunus.png'))
        self.bonus1.resize(100, 100)
        self.bonus1.move(50, 80)

        self.bonus_btn = QPushButton('', self)
        self.bonus_btn.setIcon(QIcon('./texture/menu_texture/bonus_btn'))
        self.bonus_btn.setIconSize(QSize(100, 100))
        self.bonus_btn.resize(100, 100)
        self.bonus_btn.move(50, 80)
        self.bonus_btn.clicked.connect(self.bonus)

        self.bonus_btn2 = QPushButton('', self)
        self.bonus_btn2.setIcon(QIcon('./texture/menu_texture/bonus_btn2'))
        self.bonus_btn2.setIconSize(QSize(100, 100))
        self.bonus_btn2.resize(100, 100)
        self.bonus_btn2.move(888, 10)
        self.bonus_btn2.clicked.connect(self.bonus2)

        self.bonus_btn3 = QPushButton('', self)
        self.bonus_btn3.setIcon(QIcon('./texture/menu_texture/bonus_btn3'))
        self.bonus_btn3.setIconSize(QSize(100, 100))
        self.bonus_btn3.resize(100, 100)
        self.bonus_btn3.move(150, 500)
        self.bonus_btn3.clicked.connect(self.bonus3)

        self.bonus_mouse = QLabel(self)
        self.bonus_mouse.setPixmap(QPixmap('./texture/menu_texture/bonus_btn_mouse.png'))
        self.bonus_mouse.resize(100, 100)
        self.bonus_mouse.move(self.mouse_x, self.mouse_y)

        self.bonus_mouse_btn = QPushButton(self)
        self.bonus_mouse_btn.setIcon(QIcon('./texture/menu_texture/bonus_mouse_btn'))
        self.bonus_mouse_btn.setIconSize(QSize(100, 100))
        self.bonus_mouse_btn.resize(100, 100)
        self.bonus_mouse_btn.move(self.mouse_x, self.mouse_y)
        self.bonus_mouse_btn.clicked.connect(self.bonus_mouse_def)

        self.error = QLabel(self)
        self.error.resize(200, 200)
        self.error.move(755, 490)
        self.error.setPixmap(QPixmap('./texture/menu_texture/error_texture.png'))
        self.error.hide()

        self.logo_bbz = QLabel(self)
        self.logo_bbz.move(380, 65)
        self.logo_bbz.setPixmap(QPixmap('./texture/menu_texture/bbz.png'))

        self.one_player_game = QLabel(self)
        self.one_player_game.move(180, 230)
        self.one_player_game.setPixmap(QPixmap('./texture/menu_texture/one_player.png'))

        self.two_player_game = QLabel(self)
        self.two_player_game.move(580, 230)
        self.two_player_game.setPixmap(QPixmap('./texture/menu_texture/two_player.png'))

        self.xo_btn = QPushButton('', self)
        self.xo_btn.resize(100, 100)
        self.xo_btn.move(550, 300)
        self.xo_btn.setIcon(QIcon('./texture/menu_texture/xo_logo.png'))
        self.xo_btn.setIconSize(QSize(100, 100))
        self.xo_btn.clicked.connect(self.xo_game)

        self.xo_rules = QPushButton(self)
        self.xo_rules.resize(100, 50)
        self.xo_rules.move(550, 420)
        self.xo_rules.clicked.connect(self.xo_rule)
        self.xo_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.xo_rules.setIconSize(QSize(100, 50))

        self.xo_rules_create = QLabel(self)
        self.xo_rules_create.resize(180, 200)
        self.xo_rules_create.move(510, 470)
        self.xo_rules_create.setPixmap(QPixmap('./texture/menu_texture/xo_rules.png'))
        self.xo_rules_create.hide()

        self.osu_btn = QPushButton('', self)
        self.osu_btn.resize(100, 100)
        self.osu_btn.move(350, 300)
        self.osu_btn.setIcon(QIcon('./texture/menu_texture/osu_logo.png'))
        self.osu_btn.setIconSize(QSize(100, 100))
        self.osu_btn.clicked.connect(self.osu_game)

        self.osu_rules_btn = QPushButton(self)
        self.osu_rules_btn.resize(100, 50)
        self.osu_rules_btn.move(350, 420)
        self.osu_rules_btn.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.osu_rules_btn.setIconSize(QSize(100, 50))
        self.osu_rules_btn.clicked.connect(self.osu_rules)

        self.osu_rules_create = QLabel(self)
        self.osu_rules_create.resize(180, 200)
        self.osu_rules_create.move(310, 470)
        self.osu_rules_create.setPixmap(QPixmap('./texture/menu_texture/osu_rules_texture.png'))
        self.osu_rules_create.hide()

        self.city_game_btn = QPushButton('', self)
        self.city_game_btn.resize(100, 100)
        self.city_game_btn.move(150, 300)
        self.city_game_btn.setIcon(QIcon('./texture/menu_texture/city_game_logo.png'))
        self.city_game_btn.setIconSize(QSize(100, 100))
        self.city_game_btn.clicked.connect(self.city_game)

        self.city_game_rules = QPushButton(self)
        self.city_game_rules.resize(100, 50)
        self.city_game_rules.move(150, 420)
        self.city_game_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.city_game_rules.setIconSize(QSize(100, 50))
        self.city_game_rules.clicked.connect(self.city_game_rule)

        self.city_game_rules_create = QLabel(self)
        self.city_game_rules_create.resize(180, 200)
        self.city_game_rules_create.move(110, 470)
        self.city_game_rules_create.setPixmap(QPixmap('./texture/menu_texture/city_game_rules.png'))
        self.city_game_rules_create.hide()

        self.cats_btn = QPushButton('', self)
        self.cats_btn.resize(100, 100)
        self.cats_btn.move(750, 300)
        self.cats_btn.setIcon(QIcon('./texture/menu_texture/cats_logo'))
        self.cats_btn.setIconSize(QSize(100, 100))
        self.cats_btn.clicked.connect(self.cats_game)

        self.cats_rules = QPushButton(self)
        self.cats_rules.resize(100, 50)
        self.cats_rules.move(750, 420)
        self.cats_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.cats_rules.setIconSize(QSize(100, 50))
        self.cats_rules.clicked.connect(self.cat_rules)

        self.cats_rules_create = QLabel(self)
        self.cats_rules_create.resize(180, 200)
        self.cats_rules_create.move(710, 470)
        self.cats_rules_create.setPixmap(QPixmap('./texture/menu_texture/cats_rules.png'))
        self.cats_rules_create.hide()

        self.exit_btn = QPushButton('', self)
        self.exit_btn.resize(50, 50)
        self.exit_btn.move(0, 650)
        self.exit_btn.setIcon(QIcon('./texture/menu_texture/exit_button_texture.png'))
        self.exit_btn.setIconSize(QSize(100, 50))
        self.exit_btn.clicked.connect(self.exit)

        self.setting_btn = QPushButton('', self)
        self.setting_btn.resize(50, 50)
        self.setting_btn.move(950, 650)
        self.setting_btn.setIcon(QIcon('./texture/menu_texture/crash_button.png'))
        self.setting_btn.setIconSize(QSize(90, 90))
        self.setting_btn.clicked.connect(self.setting_error)

        self.achievements_btn = QPushButton(self)
        self.achievements_btn.resize(50, 50)
        self.achievements_btn.setIcon(QIcon('./texture/menu_texture/achievements_btn_v2.png'))
        self.achievements_btn.setIconSize(QSize(50, 50))
        self.achievements_btn.clicked.connect(self.achievements)

        self.next_bbz = QPushButton(self)
        self.next_bbz.move(950, 325)
        self.next_bbz.resize(50, 50)
        self.next_bbz.setIcon(QIcon('./texture/menu_texture/next.png'))
        self.next_bbz.setIconSize(QSize(50, 50))
        self.next_bbz.clicked.connect(self.next)

        # ==============================================================================================================
        # ==============================================================================================================
        self.achievements_menu = QLabel(self)
        self.achievements_menu.resize(1000, 700)
        self.achievements_menu.setPixmap(QPixmap('./texture/menu_texture/achievements_menu.png'))
        self.achievements_menu.hide()

        self.exit_ach_btn = QPushButton(self)
        self.exit_ach_btn.resize(50, 50)
        self.exit_ach_btn.move(0, 650)
        self.exit_ach_btn.setIcon(QIcon('./texture/menu_texture/back_btn.png'))
        self.exit_ach_btn.setIconSize(QSize(50, 50))
        self.exit_ach_btn.clicked.connect(self.back)
        self.exit_ach_btn.hide()

        self.bbz_chempeon_ach = QLabel(self)
        self.bbz_chempeon_ach.resize(260, 70)
        self.bbz_chempeon_ach.move(73, 101)
        self.bbz_chempeon_ach.setPixmap(QPixmap('./texture/achievements_texture/bbz_chempion.png'))
        self.bbz_chempeon_ach.hide()

        self.mouse_hunter = QLabel(self)
        self.mouse_hunter.resize(260, 70)
        self.mouse_hunter.move(654, 101)
        self.mouse_hunter.setPixmap(QPixmap('./texture/achievements_texture/mouse_hunter.png'))
        self.mouse_hunter.hide()

        self.osu_ach = QLabel(self)
        self.osu_ach.resize(260, 70)
        self.osu_ach.move(73, 187)
        self.osu_ach.setPixmap(QPixmap('./texture/achievements_texture/osu.png'))
        self.osu_ach.hide()

        self.target = QLabel(self)
        self.target.resize(260, 70)
        self.target.move(73, 268)
        self.target.setPixmap(QPixmap('./texture/achievements_texture/right_on_target.png'))
        self.target.hide()

        self.xo_ach = QLabel(self)
        self.xo_ach.resize(260, 70)
        self.xo_ach.move(73, 349)
        self.xo_ach.setPixmap(QPixmap('./texture/achievements_texture/xo.png'))
        self.xo_ach.hide()

        self.color_ach = QLabel(self)
        self.color_ach.resize(260, 70)
        self.color_ach.move(73, 432)
        self.color_ach.setPixmap(QPixmap('./texture/achievements_texture/color_soul.png'))
        self.color_ach.hide()

        # ----------------------------------------------------------------------------------------------------

        self.cat_ach = QLabel(self)
        self.cat_ach.resize(260, 70)
        self.cat_ach.move(656, 187)
        self.cat_ach.setPixmap(QPixmap('./texture/achievements_texture/cats_played.png'))
        self.cat_ach.hide()

        self.golodomor = QLabel(self)
        self.golodomor.resize(260, 70)
        self.golodomor.move(656, 268)
        self.golodomor.setPixmap(QPixmap('./texture/achievements_texture/golodomor.png'))
        self.golodomor.hide()

        self.imposible_ach = QLabel(self)
        self.imposible_ach.resize(260, 70)
        self.imposible_ach.move(656, 349)
        self.imposible_ach.setPixmap(QPixmap('./texture/achievements_texture/imposible-posible.png'))
        self.imposible_ach.hide()

        self.last_chinese = QLabel(self)
        self.last_chinese.resize(260, 70)
        self.last_chinese.move(656, 431)
        self.last_chinese.setPixmap(QPixmap('./texture/achievements_texture/last_chinese.png'))
        self.last_chinese.hide()

        # ----------------------------------------------------------------------------------

        self.secret_hunter_ach = QLabel(self)
        self.secret_hunter_ach.resize(260, 70)
        self.secret_hunter_ach.move(73, 598)
        self.secret_hunter_ach.setPixmap(QPixmap('./texture/achievements_texture/secret_hunter.png'))
        self.secret_hunter_ach.hide()

        self.secret_rules_ach = QLabel(self)
        self.secret_rules_ach.resize(260, 70)
        self.secret_rules_ach.move(650, 598)
        self.secret_rules_ach.setPixmap(QPixmap('./texture/achievements_texture/secret_rules.png'))
        self.secret_rules_ach.hide()

        self.the_end = QLabel(self)
        self.the_end.resize(260, 70)
        self.the_end.move(363, 267)
        self.the_end.setPixmap(QPixmap('./texture/achievements_texture/the_end.png'))
        self.the_end.hide()

        # ==============================================================================================================
        # ==============================================================================================================

        # achievement
        self.muse_achievement = QPushButton(self)
        self.muse_achievement.hide()
        self.muse_achievement.resize(260, 70)
        self.muse_achievement.move(-300, 0)
        self.muse_achievement.setIcon(QIcon('./texture/achievements_texture/mouse_hunter.png'))
        self.muse_achievement.setIconSize(QSize(360, 70))
        self.muse_achievement.clicked.connect(self.secret_achievement_hunter)

        self.bbz_chempeon = QLabel(self)
        self.bbz_chempeon.resize(260, 70)
        self.bbz_chempeon.move(-300, 0)
        self.bbz_chempeon.setPixmap(QPixmap('./texture/achievements_texture/bbz_chempion.png'))

        self.secret_hunter = QLabel(self)
        self.secret_hunter.resize(260, 70)
        self.secret_hunter.move(1260, 0)
        self.secret_hunter.setPixmap(QPixmap('./texture/achievements_texture/secret_hunter.png'))

        self.secret_rules = QLabel(self)
        self.secret_rules.hide()
        self.secret_rules.resize(260, 70)
        self.secret_rules.setPixmap(QPixmap('./texture/achievements_texture/secret_rules.png'))

    def xo_rule(self):
        if not self.xo_rules_is_active:
            self.hide_ruled()
            self.xo_rules_create.show()
            self.xo_rules.setIcon(QIcon('./texture/menu_texture/rules_btn_clicced.png'))
            self.xo_rules_count += 1
            if self.xo_rules_count == 3:
                self.rules_count += 1
                self.secret_rules_check()

            self.xo_rules_is_active = True
        elif self.xo_rules_is_active:
            self.xo_rules_create.hide()
            self.xo_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
            self.xo_rules_is_active = False

    def osu_rules(self):
        if not self.osu_rules_is_active:
            self.hide_ruled()
            self.osu_rules_create.show()
            self.osu_rules_btn.setIcon(QIcon('./texture/menu_texture/rules_btn_clicced.png'))
            self.osu_rules_count += 1
            if self.osu_rules_count == 3:
                self.rules_count += 1
                self.secret_rules_check()
            self.osu_rules_is_active = True

        elif self.osu_rules_is_active:
            self.osu_rules_create.hide()
            self.osu_rules_btn.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
            self.osu_rules_is_active = False

    def city_game_rule(self):
        if not self.city_game_rules_is_active:
            self.hide_ruled()
            self.city_game_rules_create.show()
            self.city_game_rules.setIcon(QIcon('./texture/menu_texture/rules_btn_clicced.png'))
            self.city_rules_count += 1
            if self.city_rules_count == 3:
                self.rules_count += 1
                self.secret_rules_check()
            self.city_game_rules_is_active = True

        elif self.city_game_rules_is_active:
            self.city_game_rules_create.hide()
            self.city_game_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
            self.city_game_rules_is_active = False

    def cat_rules(self):
        if not self.cats_rules_is_active:
            self.hide_ruled()
            self.cats_rules_create.show()
            self.cats_rules.setIcon(QIcon('./texture/menu_texture/rules_btn_clicced.png'))
            self.cats_rules_count += 1
            if self.cats_rules_count == 3:
                self.rules_count += 1
                self.secret_rules_check()
            self.cats_rules_is_active = True
        elif self.cats_rules_is_active:
            self.cats_rules_create.hide()
            self.cats_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
            self.cats_rules_is_active = False

    def hide_ruled(self):
        self.error.hide()

        self.xo_rules_create.hide()
        self.osu_rules_create.hide()
        self.city_game_rules_create.hide()
        self.cats_rules_create.hide()

        self.xo_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.city_game_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.osu_rules_btn.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.cats_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))

        self.xo_rules_is_active = False
        self.osu_rules_is_active = False
        self.city_game_rules_is_active = False
        self.cats_rules_is_active = False

    def secret_rules_check(self):
        if (self.rules_count == 4) and not list_of_achievements[11]:
            list_of_achievements[11] = True
            self.secret_rules_def()

    def bonus(self):
        self.bonus_btn.hide()
        self.bonus_animation_wait = 1
        self.bonus1.setPixmap(QPixmap('./texture/menu_texture/bonus_btn_animation.png'))
        self.bonus_animation_timer()

    def bonus2(self):
        self.bonus_animation_wait2 = 1
        self.bonus_btn2.setIcon(QIcon('./texture/menu_texture/bonus_btn2_animation.png'))
        self.bonus_animation_timer2()

    def bonus3(self):
        self.bonus_animation_wait3 = 1
        self.bonus_btn3.setIcon(QIcon('./texture/menu_texture/bonus_btn3_animation.png'))
        self.bonus_animation_timer3()

    def bonus_animation_timer(self):
        if self.bonus_animation_wait > 0:
            self.bonus_animation_wait -= 1  # Устанавливаем значение на 1 меньше
            QTimer().singleShot(1000, self.bonus_animation_timer)
        else:
            self.bonus1.setPixmap(QPixmap('./texture/menu_texture/bunus1'))
            self.bonus_btn.show()
            self.bonus_animation_wait = 1

    def bonus_animation_timer2(self):
        if self.bonus_animation_wait2 > 0:
            self.bonus_animation_wait2 -= 1
            QTimer().singleShot(1000, self.bonus_animation_timer2)
        else:
            self.bonus_btn2.setIcon(QIcon('./texture/menu_texture/bonus_btn2'))
            self.bonus_animation_wait2 = 1

    def bonus_animation_timer3(self):
        if self.bonus_animation_wait3 > 0:
            self.bonus_animation_wait3 -= 1
            QTimer().singleShot(1000, self.bonus_animation_timer3)
        else:
            self.bonus_btn3.setIcon(QIcon('./texture/menu_texture/bonus_btn3'))
            self.bonus_animation_wait3 = 1

    def bonus_mouse_def(self):
        self.achievements_animation()
        list_of_achievements[0] = True
        self.bonus_mouse_run()

    def bonus_mouse_run(self):
        self.bonus_mouse_btn.hide()
        if self.mouse_y < 700:
            self.bonus_mouse.show()
            self.mouse_x -= 1
            self.mouse_y += 2
            self.bonus_mouse.move(self.mouse_x, self.mouse_y)
            QTimer().singleShot(10, self.bonus_mouse_run)
        else:
            self.mouse_x = 660
            self.mouse_y = -10
            if not list_of_achievements[10]:
                self.bonus_mouse.move(self.mouse_x, self.mouse_y)
                self.bonus_mouse_btn.show()
            else:
                self.bonus_mouse.hide()

    def achievements_animation(self):
        self.muse_achievement.move(0, 0)
        self.muse_achievement.show()

        animation_curve = QEasingCurve.InQuad

        animation1 = QPropertyAnimation(self.muse_achievement, b'pos', self)
        animation1.setEasingCurve(animation_curve)
        animation1.setDuration(2000)
        animation1.setKeyValueAt(0, QPoint(-300, 0))

        self.animation2 = QPropertyAnimation(self.muse_achievement, b'pos', self)
        self.animation2.setEasingCurve(animation_curve)
        self.animation2.setDuration(2000)
        self.animation2.setKeyValueAt(0, QPoint(0, 0))

        animation1.start()
        self.mouse_achievement_timer()

    def mouse_achievement_timer(self):
        if self.time > 0:
            self.time -= 1
            QTimer().singleShot(1000, self.mouse_achievement_timer)
        else:
            self.time = 4
            self.muse_achievement.move(-300, 0)
            self.animation2.start()

    def bbz_chempion_achievements(self):
        self.bbz_chempeon.move(0, 0)
        self.bbz_chempeon.show()

        animation_curve = QEasingCurve.InQuad

        animation1 = QPropertyAnimation(self.bbz_chempeon, b'pos', self)
        animation1.setEasingCurve(animation_curve)
        animation1.setDuration(2000)
        animation1.setKeyValueAt(0, QPoint(-300, 0))

        self.animation2_1 = QPropertyAnimation(self.bbz_chempeon, b'pos', self)
        self.animation2_1.setEasingCurve(animation_curve)
        self.animation2_1.setDuration(2000)
        self.animation2_1.setKeyValueAt(0, QPoint(0, 0))

        animation1.start()
        self.bbz_achievement_timer()

    def bbz_achievement_timer(self):
        if self.time_bbz_ach > 0:
            self.time_bbz_ach -= 1
            QTimer().singleShot(1000, self.bbz_achievement_timer)
        else:
            self.time_bbz_ach = 4
            self.bbz_chempeon.move(-300, 0)
            self.animation2_1.start()

    def secret_achievement_hunter(self):
        if not list_of_achievements[10]:
            list_of_achievements[10] = True
            self.secret_hunter.move(740, 0)
            self.secret_hunter.show()

            animation_curve = QEasingCurve.InQuad

            animation1 = QPropertyAnimation(self.secret_hunter, b'pos', self)
            animation1.setEasingCurve(animation_curve)
            animation1.setDuration(2000)
            animation1.setKeyValueAt(0, QPoint(1300, 0))

            self.animation2_2 = QPropertyAnimation(self.secret_hunter, b'pos', self)
            self.animation2_2.setEasingCurve(animation_curve)
            self.animation2_2.setDuration(2000)
            self.animation2_2.setKeyValueAt(0, QPoint(740, 0))

            animation1.start()
            self.secret_achievement_hunter_timer()

    def secret_achievement_hunter_timer(self):
        if self.secret_time > 0:
            self.secret_time -= 1
            QTimer().singleShot(1000, self.secret_achievement_hunter_timer)
        else:
            self.secret_time = 4
            self.secret_hunter.move(1300, 0)
            self.animation2_2.start()

    def secret_rules_def(self):
        self.secret_rules.move(740, 0)
        self.secret_rules.show()

        animation_curve = QEasingCurve.InQuad

        animation1 = QPropertyAnimation(self.secret_rules, b'pos', self)
        animation1.setEasingCurve(animation_curve)
        animation1.setDuration(2000)
        animation1.setKeyValueAt(0, QPoint(1300, 0))

        self.animation2_3 = QPropertyAnimation(self.secret_rules, b'pos', self)
        self.animation2_3.setEasingCurve(animation_curve)
        self.animation2_3.setDuration(2000)
        self.animation2_3.setKeyValueAt(0, QPoint(740, 0))

        animation1.start()
        self.secret_rules_timer()

    def secret_rules_timer(self):
        if self.secret_time > 0:
            self.secret_time -= 1
            QTimer().singleShot(1000, self.secret_rules_timer)
        else:
            self.secret_time = 4
            self.secret_rules.move(1300, 0)
            self.animation2_3.start()

    def achievements(self):
        if list_of_achievements[0] and list_of_achievements[1] \
                and list_of_achievements[2] and list_of_achievements[3] \
                and list_of_achievements[4] and list_of_achievements[5] \
                and list_of_achievements[6] and list_of_achievements[7] \
                and list_of_achievements[8] and list_of_achievements[9] \
                and list_of_achievements[10] and list_of_achievements[11]:
            list_of_achievements[12] = True
        self.achievements_menu.show()
        self.exit_ach_btn.show()
        if list_of_achievements[0]:
            self.mouse_hunter.show()
        if list_of_achievements[1]:
            self.bbz_chempeon_ach.show()
        if list_of_achievements[2]:
            self.osu_ach.show()
        if list_of_achievements[3]:
            self.target.show()
        if list_of_achievements[4]:
            self.cat_ach.show()
        if list_of_achievements[5]:
            self.golodomor.show()
        if list_of_achievements[6]:
            self.xo_ach.show()
        if list_of_achievements[7]:
            self.color_ach.show()
        if list_of_achievements[8]:
            self.imposible_ach.show()
        if list_of_achievements[9]:
            self.last_chinese.show()
        if list_of_achievements[10]:
            self.secret_hunter_ach.show()
        if list_of_achievements[11]:
            self.secret_rules_ach.show()
        if list_of_achievements[12]:
            self.the_end.show()

    def back(self):
        self.achievements_menu.hide()
        self.exit_ach_btn.hide()

        self.mouse_hunter.hide()
        self.bbz_chempeon_ach.hide()
        self.osu_ach.hide()
        self.target.hide()
        self.cat_ach.hide()
        self.golodomor.hide()
        self.xo_ach.hide()
        self.color_ach.hide()
        self.imposible_ach.hide()
        self.last_chinese.hide()
        self.secret_hunter_ach.hide()
        self.secret_rules_ach.hide()
        self.the_end.hide()

    def osu_game(self):
        self.osu_btn.setIcon(QIcon('./texture/menu_texture/osu_logo_clicced.png'))
        self.osu_game_played = True
        if self.xo_game_played and self.osu_game_played \
                and self.city_game_played and self.cats_game_played and not self.is_active:
            list_of_achievements[1] = True
            self.is_active = True
            self.bbz_chempion_achievements()
        self.hide_ruled()
        self.btn_osu_timer()

    def cats_game(self):
        self.cats_btn.setIcon(QIcon('./texture/menu_texture/cats_logo_clicced.png'))
        self.cats_game_played = True
        if self.xo_game_played and self.osu_game_played \
                and self.city_game_played and self.cats_game_played and not self.is_active:
            list_of_achievements[1] = True
            self.is_active = True
            self.bbz_chempion_achievements()
        self.hide_ruled()
        self.btn_cats_timer()

    def xo_game(self):
        self.xo_btn.setIcon(QIcon('./texture/menu_texture/xo_logo_clicced.png'))
        self.xo_game_played = True
        if self.xo_game_played and self.osu_game_played \
                and self.city_game_played and self.cats_game_played and not self.is_active:
            list_of_achievements[1] = True
            self.is_active = True
            self.bbz_chempion_achievements()
        self.hide_ruled()
        self.btn_xo_timer()

    def city_game(self):
        self.city_game_btn.setIcon(QIcon('./texture/menu_texture/city_game_logo_clicced.png'))
        self.city_game_played = True
        if self.xo_game_played and self.osu_game_played \
                and self.city_game_played and self.cats_game_played and not self.is_active:
            list_of_achievements[1] = True
            self.is_active = True
            self.bbz_chempion_achievements()
        self.btn_city_timer()

    def btn_city_timer(self):
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.btn_city_timer)
        else:
            self.city_game_btn.setIcon(QIcon('./texture/menu_texture/city_game_logo.png'))
            self.btn_time = 1

    def btn_osu_timer(self):
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.btn_osu_timer)
        else:
            self.btn_time = 1
            self.osu_btn.setIcon(QIcon('./texture/menu_texture/osu_logo.png'))
            osu_window.get_windows(list_of_windows)
            list_of_windows.setCurrentIndex(1)

    def btn_xo_timer(self):
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.btn_xo_timer)
        else:
            self.btn_time = 1
            self.xo_btn.setIcon(QIcon('./texture/menu_texture/xo_logo.png'))
            xo_window.get_windows(list_of_windows)
            list_of_windows.setCurrentIndex(4)

    def btn_cats_timer(self):
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.btn_cats_timer)
        else:
            self.btn_time = 1
            self.cats_btn.setIcon(QIcon('./texture/menu_texture/cats_logo.png'))
            cat_window.get_windows(list_of_windows)
            list_of_windows.setCurrentIndex(2)

    def setting_error(self):
        self.timer = 3
        self.hide_ruled()
        self.error.show()
        self.error_timer()

    def error_timer(self):
        if self.timer > 0:
            self.timer -= 1
            QTimer().singleShot(1000, self.error_timer)
        else:
            self.timer = 3
            self.error.hide()

    def next(self):
        bbz2_window.get_windows(list_of_windows)
        list_of_windows.setCurrentIndex(5)

    def exit(self):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    list_of_windows = QStackedWidget()

    main_window = Example()
    osu_window = Osuu(list_of_achievements)
    cat_window = Cat(list_of_achievements)
    loading_window = Loading()
    xo_window = XO_game(list_of_achievements)
    bbz2_window = BBZ2()

    list_of_windows.addWidget(main_window)  # 0
    list_of_windows.addWidget(osu_window)  # 1
    list_of_windows.addWidget(cat_window)  # 2
    list_of_windows.addWidget(loading_window)  # 3
    list_of_windows.addWidget(xo_window)  # 4
    list_of_windows.addWidget(bbz2_window)  # 5

    list_of_windows.setWindowTitle('BBZ_game')
    list_of_windows.setWindowIcon(QIcon('./texture/menu_texture/game_logo'))

    loading_window.get_windows(list_of_windows)
    list_of_windows.setCurrentIndex(3)

    list_of_windows.resize(1000, 700)
    list_of_windows.setFixedSize(1000, 700)
    list_of_windows.adjustSize()
    list_of_windows.clearFocus()
    list_of_windows.show()
    sys.exit(app.exec())
