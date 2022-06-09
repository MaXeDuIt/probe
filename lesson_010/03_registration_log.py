# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class CheckReg:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_content = None
        self.line = None
        self.user_name = None
        self.user_mail = None
        self.user_age = None

    def open_file(self):
        self.file_content = open(self.file_name, 'r', encoding='utf8')

    def close_file(self):
        self.file_content.close()

    def write_file(self):
        self.file_content.write(self.line)

    def split_file(self):
        for line in self.file_content:
            self.user_name, self.user_mail, self.user_age = line.split(' ')
            print(f"### {self.user_name} ### {self.user_mail} ### {self.user_age}")


check_reg = CheckReg('registrations.txt')
check_reg.open_file()
check_reg.split_file()
check_reg.close_file()
