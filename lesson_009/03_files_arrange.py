# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import time
import os
import zipfile


class Arrange:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_time = None

    def search(self):
        for dirpath, dirnames, filenames in os.walk(self.file_name):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                self.file_time = time.gmtime(secs)
                year = self.file_time[0]
                month = self.file_time[1]
                self.creation_dir(folder=year, subfolder=month)

    def creation_dir(self, folder, subfolder):
        self.folder = folder
        self.subfolder = subfolder
        os.makedirs(f"icons_by_year\\{self.folder}\\{self.subfolder}")

icons = Arrange('icons')
icons.search()



# zfile = zipfile.ZipFile('icons.zip', 'r')
# for file_info in zfile.infolist():
#     print(file_info.filename, file_info.date_time, file_info.file_size)




# path = 'C:/Windows/help'
# path_normalized = os.path.normpath(path)
# print(path_normalized)
#
# count = 0
# for dirpath, dirnames, filenames in os.walk(path_normalized):
#     print('*' * 27)
#     print(dirpath, dirnames, filenames)
#     print(os.path.dirname(dirpath))
#     count += len(filenames)
#     for file in filenames:
#         full_file_path = os.path.join(dirpath, file)
#         secs = os.path.getmtime(full_file_path)
#         file_time = time.gmtime(secs)
#         if file_time[0] == 2013:
#             # выводим только файлы за 2013 год
#             print(full_file_path, secs, file_time)
# print(count)
#
# print(__file__, os.path.dirname(__file__))


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
