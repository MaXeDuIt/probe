# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness_for_man = 50
        self.food_for_man = 20
        self.money = 50

    def __str__(self):
        return 'Я {}, сытость {}, еда {}, деньги {}'.format(
            self.name, self.fullness_for_man, self.food_for_man, self.money)

    def go_to_work(self):
        cprint('{} сходил на работу и заработал деньги'.format(self.name), color='blue')
        self.money += 150
        self.fullness_for_man -= 10

    def eat(self):
        if self.food_for_man >= 10:
            cprint('{} поел'.format(self.name), color='green')
            self.fullness_for_man += 30
            self.food_for_man -= 20
        else:
            cprint('Еда закончилась, нужно сходить в магазин', color='red')

    def shopping(self):
        if self.money >= 50:
            cprint('{} сходил в магазин и купил еду'.format(self.name), color='magenta')
            self.food_for_man += 50
            self.money -= 50
        else:
            cprint('Закончились деньги, нужно идти на работу', color='red')

    def read_book(self):
        cprint('{} читал книги весь день'.format(self.name), color='yellow')
        self.fullness_for_man -= 20

    def act(self):
        if self.fullness_for_man <= 0:
            cprint('{} умер'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness_for_man <= 20:
            self.eat()
        elif self.food_for_man < 10:
            self.shopping()
        elif self.money < 50:
            self.go_to_work()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.go_to_work()
        else:
            self.read_book()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness_for_cat = 50
        self.food_for_cat = 20
        self.dirt = 0

    def __str__(self):
        return 'Я кот {}, сытость {}, еда {}'.format(
            self.name, self.fullness_for_cat, self.food_for_cat)

    def eat(self):
        if self.food_for_cat >= 10:
            cprint('{} поел'.format(self.name), color='green')
            self.fullness_for_cat += 20
            self.food_for_cat -= 10
        else:
            cprint('Нужно отправить хозяина за кормом, а пока подеру-ка я обои', color='red')
            self.fullness_for_cat -= 10
            self.dirt += 10

    def sleap(self):
        cprint('{} спал весь день'.format(self.name), color='yellow')
        self.fullness_for_cat -= 10

    def tears_the_wallpaper(self):
        cprint('{} подрал обои'.format(self.name), color='blue')
        self.fullness_for_cat -= 20
        self.dirt += 5

    def act(self):
        if self.fullness_for_cat <= 0:
            cprint('{} умер'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness_for_cat <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.tears_the_wallpaper()
        else:
            self.sleap()


# maxim = Man('Максим')
# for day in range(1, 366):
#     cprint('_______________ день {} _______________'.format(day), color='cyan')
#     maxim.act()
#     cprint('__________ в конце дня __________', color='grey')
#     print(maxim)

pushok = Cat('Пушок')
for day in range(1, 21):
    cprint('_______________ день {} _______________'.format(day), color='cyan')
    pushok.act()
    print(pushok)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
