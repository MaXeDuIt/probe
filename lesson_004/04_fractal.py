# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

sd.resolution = (1200, 1000)

root_point = sd.get_point(600, 30)

# def draw_branches(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#     v1.draw()
#
#     next_point_1 = v1.end_point
#     next_angle_1 = angle - 30
#     next_length_1 = length * .75
#     v1 = sd.get_vector(start_point=next_point_1, angle=next_angle_1, length=next_length_1)
#     v1.draw()
#
#     next_point_1 = v1.end_point
#     next_angle_1 = next_angle_1 - 30
#     next_length_1 = next_length_1 * .75
#     v1 = sd.get_vector(start_point=next_point_1, angle=next_angle_1, length=next_length_1)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=point, angle=angle, length=length)
#     v2.draw()
#
#     next_point_2 = v2.end_point
#     next_angle_2 = angle + 30
#     next_length_2 = length * .75
#     v2 = sd.get_vector(start_point=next_point_2, angle=next_angle_2, length=next_length_2)
#     v2.draw()
#
#     next_point_2 = v2.end_point
#     next_angle_2 = next_angle_2 + 30
#     next_length_2 = next_length_2 * .75
#     v2 = sd.get_vector(start_point=next_point_2, angle=next_angle_2, length=next_length_2)
#     v2.draw()
#
# draw_branches(point=root_point, angle=90, length=200)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# def draw_branches(point, angle, length):
#     if length < 9:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#     v1.draw()
#
#     next_point_1 = v1.end_point
#     next_angle_1 = angle - 30
#     next_length_1 = length * .75
#     v1 = sd.get_vector(start_point=next_point_1, angle=next_angle_1, length=next_length_1)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=point, angle=angle, length=length)
#     v2.draw()
#
#     next_point_2 = v2.end_point
#     next_angle_2 = angle + 30
#     next_length_2 = length * .75
#     v2 = sd.get_vector(start_point=next_point_2, angle=next_angle_2, length=next_length_2)
#     v2.draw()
#
#     draw_branches(point=next_point_1, angle=next_angle_1, length=next_length_1)
#     draw_branches(point=next_point_2, angle=next_angle_2, length=next_length_2)
#
# draw_branches(point=root_point, angle=90, length=200)

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

def draw_branches(point, angle, length):
# Условие для выхода функции (длина меньше 5 пикселей) - иначе бесконечность
    if length < 5:
        return
# Опеределяю рандомные коэффициенты для изменения угла и длины ветки alpha, delta
    alpha = sd.random_number(a=18, b=42)
    delta = sd.random_number(a=60, b=90) / 100
# Рисую главный вектор_1 (ствол)
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
# Начинаю рисовать ветки, применяю коэф. для угла и длины веток, следующая точка вектора_1 - конец предыдущего_1
    next_point_1 = v1.end_point
    next_angle_1 = angle - alpha
    next_length_1 = length * delta
    v1 = sd.get_vector(start_point=next_point_1, angle=next_angle_1, length=next_length_1)
    v1.draw()
# Рисую главный вектор_2 (ствол) - повторяется с вектором_1
    v2 = sd.get_vector(start_point=point, angle=angle, length=length)
    v2.draw()
# Начинаю рисовать ветки, применяю коэф. для угла и длины веток, следующая точка вектора_2 - конец предыдущего_2
    next_point_2 = v2.end_point
    next_angle_2 = angle + alpha
    next_length_2 = length * delta
    v2 = sd.get_vector(start_point=next_point_2, angle=next_angle_2, length=next_length_2)
    v2.draw()
# Рекурсия - вызываю функцию внутри функции (с отрисовкой двух веток)
    draw_branches(point=next_point_1, angle=next_angle_1, length=next_length_1)
    draw_branches(point=next_point_2, angle=next_angle_2, length=next_length_2)


draw_branches(point=root_point, angle=90, length=200)

# Пригодятся функции
# sd.random_number()

sd.pause()


