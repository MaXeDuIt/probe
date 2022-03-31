# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_x = 50
end_x = 350
step_x = 30
for _ in range(7):
    start_point = sd.get_point(start_x, 50)
    end_point = sd.get_point(end_x, 450)
    sd.line(start_point, end_point, color=rainbow_colors[_], width=30)
    start_x += step_x
    end_x += step_x

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
def rainbow(point, step):
    radius = 500
    for _ in range(7):
        radius += step
        sd.circle(center_position=point, radius=radius, color=rainbow_colors[_], width=20)

point = sd.get_point(375, -150)
rainbow(point, 20)

sd.pause()
