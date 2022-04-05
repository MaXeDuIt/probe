# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

forms = {'1': 'Треугольник', '2': 'Квадрат', '3': 'Пятиугольник', '4': 'Шестиугольник'}
#Создал словарь для распаковки **kwargs

# Функция треугольника
def triangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle - 120, length=length, width=3)
    v3.draw()

# Функция квадрата
def quadrate(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw()

# Функция пятиугольника
def pentagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw()
    sd.line(start_point=v4.end_point, end_point=v1.start_point, width=3)

# Функция шестиугольника
def hexagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw()
    sd.line(start_point=v5.end_point, end_point=v1.start_point, width=3)

# Функция отрисовки фигуры
def form_chois(form):
    if form == '1':
        point = sd.get_point(300, 300)
        triangle(point=point, angle=30, length=100)
    elif form == '2':
        point = sd.get_point(300, 300)
        quadrate(point=point, angle=30, length=90)
    elif form == '3':
        point = sd.get_point(300, 300)
        pentagon(point=point, angle=30, length=85)
    elif form == '4':
        point = sd.get_point(300, 300)
        hexagon(point=point, angle=30, length=80)

# Функция распоковки словаря colors
def print_forms(**kwargs):
    print('Возможные фигуры:')
    for key, value in kwargs.items():
        print(key, ':', value)

print_forms(**forms)
# Вызвал функцию распаковки

while True:
    form = input('Введите желаемую фигуру > ')
    if form in forms:
        print(forms[form])
        form_chois(form)
        break
    else:
        print('Вы ввели некорректный номер!')
# Тело цикло while смысл - если номер фигуры правильный (из словаря forms), то вызываем функцию отрисовки фигуры
#                                                                                   и прекращаем цикл
#                           если нет, то повторяем запрос

sd.pause()
