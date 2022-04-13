import simple_draw as sd

root_point = sd.get_point(600, 30)

def draw_branches(point, angle, length):
# Условие для выхода функции (длина меньше 5 пикселей) - иначе бесконечность
    if length < 5:
        return
# Опеределяю рандомные коэффициенты для изменения угла и длины ветки alpha, delta
    alpha = sd.random_number(a=18, b=42)
    delta = sd.random_number(a=60, b=90) / 100
# Рисую главный вектор_1 (ствол)
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=sd.COLOR_PURPLE)
# Начинаю рисовать ветки, применяю коэф. для угла и длины веток, следующая точка вектора_1 - конец предыдущего_1
    next_point_1 = v1.end_point
    next_angle_1 = angle - alpha
    next_length_1 = length * delta
    v1 = sd.get_vector(start_point=next_point_1, angle=next_angle_1, length=next_length_1)
    v1.draw(color=sd.COLOR_PURPLE)
# Рисую главный вектор_2 (ствол) - повторяется с вектором_1
    v2 = sd.get_vector(start_point=point, angle=angle, length=length)
    v2.draw(color=sd.COLOR_DARK_YELLOW)
# Начинаю рисовать ветки, применяю коэф. для угла и длины веток, следующая точка вектора_2 - конец предыдущего_2
    next_point_2 = v2.end_point
    next_angle_2 = angle + alpha
    next_length_2 = length * delta
    v2 = sd.get_vector(start_point=next_point_2, angle=next_angle_2, length=next_length_2)
    v2.draw(color=sd.COLOR_DARK_YELLOW)
# Рекурсия - вызываю функцию внутри функции (с отрисовкой двух веток)
    draw_branches(point=next_point_1, angle=next_angle_1, length=next_length_1)
    draw_branches(point=next_point_2, angle=next_angle_2, length=next_length_2)


