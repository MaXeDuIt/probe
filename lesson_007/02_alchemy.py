# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        pass

    def __str__(self):
        pass


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        pass

    def __str__(self):
        pass


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        pass

    def __str__(self):
        pass


class Earth:

    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        pass

    def __str__(self):
        pass


class Storm:

    def __init__(self):
        self.name = 'Шторм'


class Steam:

    def __init__(self):
        self.name = 'Пар'


class Mud:

    def __init__(self):
        self.name = 'Грязь'


class Lightning:

    def __init__(self):
        self.name = 'Молния'

class Dust:

    def __init__(self):
        self.name = 'Пыль'

class Lava:

    def __init__(self):
        self.name = 'Лава'



# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
