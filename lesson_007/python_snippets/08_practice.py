# -*- coding: utf-8 -*-

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food_cat >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food_cat -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food_cat += 50
        else:
            cprint('{} деньги кончились'.format(self.name), color='red')

    def go_into_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food_cat < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

class House:

    def __init__(self):
        self.name = 'Квартира'

    def refrigerator(self):
        self.food = 10

    def locker(self):
        self.money = 50

    def __str__(self):
        return 'В доме {}, в холодильнике осталось еды {}, в тумбочке денег осталось {}'.format(
            self.name, self.food, self.money)



citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни')
]

my_sweet_home = House()
my_sweet_home.refrigerator()
my_sweet_home.locker()
for citizen in citizens:
    citizen.go_into_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} ================='.format(day))
    for citizen in citizens:
        citizen.act()
    print('================= в конце дня ===============')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
