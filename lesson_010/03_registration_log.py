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


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check_reg(line):
    user_name, user_mail, user_age = line.split(' ')
    symbols = ('@', '.')
    if user_name.isalpha() is False:
        raise NotNameError
    elif int(user_age) not in range(10, 100):
        raise ValueError
    elif user_name and user_mail and user_age is False:
        raise TypeError
    else:
        for char in symbols:
            if char not in user_mail:
                raise NotEmailError
    return line

with open('registrations.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line[:-1]
        try:
            check_reg(line)
        except NotNameError:
            bad = open('registrations_bad.txt', 'a', encoding='utf8')
            bad.write(f"{line} Поле имени содержит НЕ только буквы\n")
            bad.close()
        except NotEmailError:
            bad = open('registrations_bad.txt', 'a', encoding='utf8')
            bad.write(f"{line} Поле емейл НЕ содержит @ и .(точку)\n")
            bad.close()
        except ValueError:
            bad = open('registrations_bad.txt', 'a', encoding='utf8')
            bad.write(f"{line} Поле возраст НЕ является числом от 10 до 99\n")
            bad.close()
        except TypeError:
            bad = open('registrations_bad.txt', 'a', encoding='utf8')
            bad.write(f"{line} Присутсвуют НЕ все три поля\n")
            bad.close()
        else:
            good = open('registrations_good.txt', 'a', encoding='utf8')
            good.write(f"{line}\n")
            good.close()

file.close()