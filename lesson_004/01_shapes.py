# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def triangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.COLOR_GREEN)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw(color=sd.COLOR_GREEN)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle - 120, length=length, width=3)
    v3.draw(color=sd.COLOR_GREEN)

point = sd.get_point(150, 400)
triangle(point=point, angle=45, length=100)

def quadrate(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.COLOR_RED)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw(color=sd.COLOR_RED)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw(color=sd.COLOR_RED)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw(color=sd.COLOR_RED)

point = sd.get_point(400, 400)
quadrate(point=point, angle=30, length=90)

def pentagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.COLOR_ORANGE)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw(color=sd.COLOR_ORANGE)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw(color=sd.COLOR_ORANGE)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw(color=sd.COLOR_ORANGE)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    v5.draw(color=sd.COLOR_ORANGE)

point = sd.get_point(150, 100)
pentagon(point=point, angle=45, length=85)

def hexagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.COLOR_PURPLE)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw(color=sd.COLOR_PURPLE)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw(color=sd.COLOR_PURPLE)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw(color=sd.COLOR_PURPLE)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw(color=sd.COLOR_PURPLE)
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    v6.draw(color=sd.COLOR_PURPLE)

point = sd.get_point(450, 100)
hexagon(point=point, angle=45, length=80)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
