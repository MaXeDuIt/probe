# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Parser:

    def __init__(self, file_name_in, file_name_out):
        self.file_name_in = file_name_in
        self.file_name_out = file_name_out
        self.file_in = None
        self.file_out = None
        self.line = None
        self.prev_line = ''
        self.line_for_write = ''
        self.count = 1

    def file_open(self):
        self.file_in = open(self.file_name_in, 'r')
        self.file_out = open(self.file_name_out, 'w')
        return self.file_in, self.file_out

    def close_file(self):
        self.file_in.close()
        self.file_out.close()

    def write_file(self):
        self.line_for_write = f"{self.prev_line} {self.count}\n"
        self.file_out.write(self.line_for_write)

    def act(self):
        for self.line in self.file_in:
            self.line = self.line[:-1]
            if self.line.endswith('NOK'):
                self.line = self.line[1:17]
                if self.line == self.prev_line:
                    self.count += 1
                else:
                    if self.prev_line:
                        line_for_write = f"{self.prev_line} {self.count}\n"
                        self.file_out.write(line_for_write)
                        print(self.prev_line, self.count)
                        self.count = 1
                self.prev_line = self.line


parser = Parser(file_name_in='events.txt', file_name_out='02_out.txt')
parser.file_open()
parser.act()
parser.close_file()




# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
