# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y, color):
    start_point = sd.get_point(x, y)

    sd.circle(start_point, 50, color=color, width=3)

    sd.circle(sd.get_point(x + 15, y + 20), 5, color=color, width=3)

    sd.circle(sd.get_point(x - 15, y + 20), 5, color=color, width=3)

    sd.line(sd.get_point(x, y + 5), sd.get_point(x, y - 10), color=color, width=3)

    sd.line(sd.get_point(x, y + 40), sd.get_point(x, y + 80), color=color, width=3)

    sd.line(sd.get_point(x - 15, y + 40), sd.get_point(x - 30, y + 80), color=color, width=3)

    sd.line(sd.get_point(x + 15, y + 40), sd.get_point(x + 30, y + 80), color=color, width=3)

    sd.line(sd.get_point(x - 10, y - 25), sd.get_point(x + 10, y - 25), color=color, width=3)

    sd.line(sd.get_point(x - 10, y - 25), sd.get_point(x - 20, y - 20), color=color, width=3)

    sd.line(sd.get_point(x + 10, y - 25), sd.get_point(x + 20, y - 20), color=color, width=3)

for i in range(10):
    point = sd.random_point()
    x = point.x
    y = point.y
    color = sd.random_color()
    smile(x, y, color)

sd.pause()
