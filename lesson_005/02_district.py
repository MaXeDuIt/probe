# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as h1r1, room2 as h1r2
from district.central_street.house2 import room1 as h2r1, room2 as h2r2
residents = []
for i in h1r1.folks:
    residents.append(i)
for i in h1r2.folks:
    residents.append(i)
for i in h2r1.folks:
    residents.append(i)
for i in h2r2.folks:
    residents.append(i)

print('На районе живут:', ', '.join(residents))