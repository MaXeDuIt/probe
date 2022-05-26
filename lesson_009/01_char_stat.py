# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Letter:
    total_char = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.sorted_stat = {}

    def open(self):
        self.file = open(self.file_name, 'r', encoding='cp1251')
        return self.file

    def collect(self):
        for line in self.file:
            for char in line:
                if char.isalpha():
                    self.total_char += 1
                    if char in self.stat:
                        self.stat[char] += 1
                    else:
                        self.stat[char] = 1

    def sort(self):
        self.sorted_keys = sorted(self.stat, key=self.stat.get, reverse=True)
        for char in self.sorted_keys:
            self.sorted_stat[char] = self.stat[char]

    def printing(self):
        print(f"{'+':-<16}{'+':-<16}{'+'}")
        print(f"|{'Буква':^15}|{'Частота':^15}|")
        print(f"{'+':-<16}{'+':-<16}{'+'}")
        for char, count in self.sorted_stat.items():
            print(f'|{char:^15}|{count:^15d}|')
        print(f"{'+':-<16}{'+':-<16}{'+'}")
        print(f"|{'Итого':^15}|{self.total_char:^15}|")
        print(f"{'+':-<16}{'+':-<16}{'+'}")

    def closing(self):
        self.file.close()


letter = Letter(file_name='python_snippets\\voyna-i-mir.txt')
letter.open()
letter.collect()
letter.closing()
letter.sort()
letter.printing()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
