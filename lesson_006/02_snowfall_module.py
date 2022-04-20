# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

from snowfall import create_snowfall, draw_snowfall, move_snowfall, number_of_snowfall, delete_snowfall, \
    coordinates, colors


# создать_снежинки(N)
N = int(input('Введите количество снежинок: '))
create_snowfall(N)
color = input('Введите цвет снежинок: ')
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowfall(color=sd.background_color)
    #  сдвинуть_снежинки()
    move_snowfall()
    #  нарисовать_снежинки_цветом(color)
    draw_snowfall(color=colors[color])
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
