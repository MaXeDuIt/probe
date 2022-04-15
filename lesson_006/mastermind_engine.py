from random import sample

_number = []


def make_a_number():
    global _number
    _number = []
    _number = str(sample(range(0, 9), k=4))
    print(_number)


def check_a_number():
    pass



