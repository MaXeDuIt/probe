# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for y in range(0, 700, 50):
    for x in range(0, 700, 100):
        point_1 = simple_draw.get_point(x, y)
        point_2 = simple_draw.get_point(x, y+50)
        simple_draw.line(start_point=point_1, end_point=point_2, color=simple_draw.COLOR_DARK_YELLOW, width=1)

for x in range(0, 700, 100):
    for y in range(0, 700, 50):
        point_1 = simple_draw.get_point(x, y)
        point_2 = simple_draw.get_point(x+100, y)
        simple_draw.line(start_point=point_1, end_point=point_2, color=simple_draw.COLOR_DARK_YELLOW, width=1)

simple_draw.pause()
