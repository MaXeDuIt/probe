# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_polygon(point, angle, length):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v.draw()
        for i in range(n - 1):
            angle += 360 / n
            v = sd.get_vector(start_point=v.end_point, angle=angle, length=length, width=3)
            v.draw()
    return draw_polygon


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

draw_quadrate = get_polygon(n=4)
draw_quadrate(point=sd.get_point(200, 400), angle=33, length=100)

draw_pentagon = get_polygon(n=5)
draw_pentagon(point=sd.get_point(400, 200), angle=43, length=100)

draw_hexagon = get_polygon(n=6)
draw_hexagon(point=sd.get_point(400, 400), angle=53, length=75)

sd.pause()
