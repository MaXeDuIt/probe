# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.


import simple_draw as sd
from morning_in_the_village import house, land, wall, rainbow, tree, human, sun, snow

sd.resolution = (1500, 600)

house.house()
land.land()
wall.wall()
rainbow.rainbow(sd.get_point(615, 0), 20)
tree.draw_branches(point=sd.get_point(1000, 100), angle=90, length=85)
tree.draw_branches(point=sd.get_point(1300, 75), angle=90, length=45)
tree.draw_branches(point=sd.get_point(1300, 300), angle=90, length=35)
tree.draw_branches(point=sd.get_point(1250, 475), angle=90, length=30)
human.human(1100, 150)
sun.sun(200, 450)
snow.snow(30)

sd.pause()