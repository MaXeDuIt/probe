# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y):
    point = simple_draw.get_point(x, y)
    radius = 50
    simple_draw.circle(center_position=point, radius=radius, width=2)
    point = simple_draw.get_point(x + 15, y + 20)
    radius = 5
    simple_draw.circle(center_position=point, radius=radius, width=2)
    point = simple_draw.get_point(x - 15, y + 20)
    radius = 5
    simple_draw.circle(center_position=point, radius=radius, width=2)





#    def bubble(point, step):
#        radius = 50
#        for _ in range(3):
#            radius += step
#            sd.circle(center_position=point, radius=radius, width=2)
#
#    point = sd.get_point(300, 300)
#    bubble(point=point, step=10)
smile(100, 100)

simple_draw.pause()
