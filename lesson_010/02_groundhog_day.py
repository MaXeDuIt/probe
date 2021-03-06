# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint, choice


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


ENLIGHTENMENT_CARMA_LEVEL = 777
total_carma = 0
event = [IamGodError, CarCrashError, DepressionError, DrunkError, GluttonyError, SuicideError]
log = open('02_log.txt', 'w')
days = 1

def one_day():
    carma_day = randint(1, 7)
    dice = randint(1, 13)
    day_event = choice(event)
    if dice == 7:
        try:
            log.write(f"{day_event}\n")
            raise day_event
        except day_event:
            print(f"Сегодня произошло событие {day_event}")
    return carma_day


while total_carma < ENLIGHTENMENT_CARMA_LEVEL:
    print(f"День номер {days}")
    print(total_carma)
    total_carma += one_day()
    days += 1
else:
    print(f"Карма заполнена, выход из временной петли. Дней потрачено - {days}")
    log.close()


# https://goo.gl/JnsDqu
