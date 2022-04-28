# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


# class Snowflake:
#
#     def __init__(self):
#         self.x = sd.random_number(100, 500)
#         self.y = sd.random_number(400, 500)
#         self.length = sd.random_number(25, 60)
#         self.f_a = sd.random_number(1, 8)/10
#         self.f_b = sd.random_number(1, 7)/10
#         self.f_c = sd.random_number(35, 65)
#
#     def clear_previous_picture(self):
#         sd.start_drawing()
#         self.point = sd.get_point(self.x, self.y)
#         self.color = sd.background_color
#         sd.snowflake(center=self.point, length=self.length, color=self.color,
#                      factor_a=self.f_a, factor_b=self.f_b, factor_c=self.f_c)
#         sd.finish_drawing()
#
#     def move(self):
#         self.x += sd.random_number(-10, 10)
#         self.y -= sd.random_number(5, 15)
#
#     def draw(self):
#         sd.start_drawing()
#         self.point = sd.get_point(self.x, self.y)
#         self.color = sd.COLOR_WHITE
#         sd.snowflake(center=self.point, length=self.length, color=self.color,
#                      factor_a=self.f_a, factor_b=self.f_b, factor_c=self.f_c)
#         sd.finish_drawing()
#
#     def can_fall(self):
#         return self.y > 15
#
#
# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

class Snowflake:

    def __init__(self):
        self.x = sd.random_number(100, 500)
        self.y = sd.random_number(400, 500)
        self.length = sd.random_number(25, 60)
        self.f_a = sd.random_number(1, 8)/10
        self.f_b = sd.random_number(1, 7)/10
        self.f_c = sd.random_number(35, 65)

    def clear_previous_picture(self):
        sd.start_drawing()
        self.point = sd.get_point(self.x, self.y)
        self.color = sd.background_color
        sd.snowflake(center=self.point, length=self.length, color=self.color,
                     factor_a=self.f_a, factor_b=self.f_b, factor_c=self.f_c)
        sd.finish_drawing()

    def move(self):
        self.x += sd.random_number(-10, 10)
        self.y -= sd.random_number(5, 15)

    def draw(self):
        sd.start_drawing()
        self.point = sd.get_point(self.x, self.y)
        self.color = sd.COLOR_WHITE
        sd.snowflake(center=self.point, length=self.length, color=self.color,
                     factor_a=self.f_a, factor_b=self.f_b, factor_c=self.f_c)
        sd.finish_drawing()

    def can_fall(self):
        return self.y > 15

    def get_flakes(self, count):
        global flakes_list
        flakes_list = []
        for i in range(count):
            flakes_list.append(Snowflake())
        return flakes_list

    def get_fallen_flakes(self):
        global count_fallen_flakes
        if self.y < 15:
            count_fallen_flakes += 1
        print(count_fallen_flakes)
        return count_fallen_flakes

    def append_flakes(self, count):



count_fallen_flakes = 0
flake = Snowflake()

flakes = flake.get_flakes(5)
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = flake.get_fallen_flakes()
    if fallen_flakes:
        flake.append_flakes(count=fallen_flakes)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
