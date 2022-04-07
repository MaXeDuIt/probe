# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 5

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

for element in range(N):
    x = sd.random_number(100, 1100)
    y = sd.random_number(400, 550)
    elements = (x, y)
    coordinates = [elements]
    print(coordinates)
    for x, y in coordinates:
        length = sd.random_number(10, 100)
        sd.start_drawing()
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
        while True:
            sd.snowflake(center=point, length=length, color=sd.background_color)
            y -= 20
            x += sd.random_number(-25, 25)
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
            if y < 50:
                break
            sd.finish_drawing()
            sd.sleep(0.1)
            if sd.user_want_exit():
                break

sd.pause()

#             sd.clear_screen()
#             point = sd.get_point(x, y)
#             sd.snowflake(center=point, length=length)
#             y -= 25
#             if y < 50:
#                 break
#             x += sd.random_number(-20, 20)
#             sd.sleep(0.1)
#             if sd.user_want_exit():
#                 break

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
