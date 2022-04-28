# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    x = sd.random_number(100, 500)
    y = sd.random_number(400, 500)
    length = sd.random_number(25, 60)
    f_a = sd.random_number(1, 8)/10
    f_b = sd.random_number(1, 7)/10
    f_c = sd.random_number(35, 65)

    def __init__(self):
        self.name = 'снежинка'
        self.coordinates = sd.get_point(Snowflake.x, Snowflake.y)

    def clear_previous_picture(self):
        sd.snowflake(center=self.coordinates, length=Snowflake.length, color=sd.background_color,
                     factor_a=Snowflake.f_a, factor_b=Snowflake.f_b, factor_c=Snowflake.f_c)

    def move(self):
        Snowflake.x += sd.random_number(-10, 10)
        Snowflake.y -= sd.random_number(5, 15)
        self.coordinates = sd.get_point(Snowflake.x, Snowflake.y)

    def draw(self):
        sd.snowflake(center=self.coordinates, length=Snowflake.length, color=sd.COLOR_WHITE,
                     factor_a=Snowflake.f_a, factor_b=Snowflake.f_b, factor_c=Snowflake.f_c)

    def can_fall(self):
        return Snowflake.y > 15


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

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

sd.pause()
