# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 100

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
coordinates = {}
for i in range(N):
    coordinates[i] = {}
    coordinates[i]['x'] = sd.random_number(0, 1200)
    coordinates[i]['y'] = 700
    coordinates[i]['length'] = sd.random_number(3, 17)
    coordinates[i]['f_a'] = sd.random_number(1, 8)/10
    coordinates[i]['f_b'] = sd.random_number(1, 7)/10
    coordinates[i]['f_c'] = sd.random_number(35, 65)
    coordinates[i]['wind'] = sd.random_number(3, 17)
# Создаю словарь со списком координат x, y, length, factor_a, factor_b, factor_c

while True:
    sd.start_drawing()              # начинаем рисование без очистки экрана
    for i, coordinates_item in coordinates.items():
        point = sd.get_point(coordinates_item['x'], coordinates_item['y'])
        sd.snowflake(center=point, length=coordinates_item['length'], color=sd.background_color,
                     factor_a=coordinates_item['f_a'], factor_b=coordinates_item['f_b'],
                     factor_c=coordinates_item['f_c'])             # рисуем снежинку цветом backround
        coordinates_item['y'] -= coordinates_item['wind']
        coordinates_item['x'] += sd.random_number(-15, 15)         # меняем координаты x, y (смещение снежинки)
        point = sd.get_point(coordinates_item['x'], coordinates_item['y']) # получаем новую точку рисования
        sd.snowflake(center=point, length=coordinates_item['length'], color=sd.COLOR_WHITE,     # рисуем новую снежинку
                     factor_a=coordinates_item['f_a'], factor_b=coordinates_item['f_b'],        # белым цветом
                     factor_c=coordinates_item['f_c'])
        if coordinates_item['y'] < 10:
            sd.snowflake(center=point, length=coordinates_item['length'], color=sd.COLOR_WHITE,
                         factor_a=coordinates_item['f_a'], factor_b=coordinates_item['f_b'],
                         factor_c=coordinates_item['f_c'])
            coordinates_item['y'] = 700                            # запускаем бесконечность падения снежинок
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

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
