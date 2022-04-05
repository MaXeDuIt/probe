# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

colors = {'1': 'RED', '2': 'ORANGE', '3': 'YELLOW', '4': 'GREEN', '5': 'CYAN', '6': 'BLUE', '7': 'PURPLE'}
#Создал словарь для распаковки **kwargs

color_chois = {'1': sd.COLOR_RED, '2': sd.COLOR_ORANGE, '3': sd.COLOR_YELLOW, '4': sd.COLOR_GREEN,
               '5': sd.COLOR_CYAN, '6': sd.COLOR_BLUE, '7': sd.COLOR_PURPLE}
#Создал словарь для выбора цвета в цикле while

# Функция треугольника
def triangle(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle - 120, length=length, width=3)
    v3.draw(color=color)

# Функция квадрата
def quadrate(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw(color=color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw(color=color)

# Функция пятиугольника
def pentagon(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw(color=color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw(color=color)
    sd.line(start_point=v4.end_point, end_point=v1.start_point, color=color, width=3)

# Функция шестиугольника
def hexagon(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw(color=color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw(color=color)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw(color=color)
    sd.line(start_point=v5.end_point, end_point=v1.start_point, color=color, width=3)

# Функция распоковки словаря colors
def print_colors(**kwargs):
    print('Возможные цвета:')
    for key, value in kwargs.items():
        print(key, ':', value)

print_colors(**colors)
# Вызвал функцию распаковки

while True:
    color = input('Введите желаемый цвет > ')
    if color in colors:
        print(colors[color])
        point = sd.get_point(150, 400)
        triangle(point=point, angle=45, length=100, color=color_chois[color])
        point = sd.get_point(400, 400)
        quadrate(point=point, angle=30, length=90, color=color_chois[color])
        point = sd.get_point(150, 100)
        pentagon(point=point, angle=45, length=85, color=color_chois[color])
        point = sd.get_point(450, 100)
        hexagon(point=point, angle=45, length=80, color=color_chois[color])
        break
    else:
        print('Вы ввели некорректный номер!')
# Тело цикло while смысл - если номер цвета правильный (из словаря color_chois), то вызываем функции фигур
#                                                                                   и прекращаем цикл
#                           если нет, то повторяем запрос


sd.pause()
