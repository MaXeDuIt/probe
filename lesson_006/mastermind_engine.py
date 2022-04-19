from random import sample

bull = 0
cow = 0
bulls_and_cows = {'bulls': bull, 'cows': cow}


def make_a_number():
    global number
    number = list(sample(range(0, 9), k=4))
    # print('Загаданное число равно', number)
    return number


def check_a_number(number_check):
    bull = 0
    cow = 0
    bulls_and_cows.update({'bulls': bull, 'cows': cow})
    # print(number_check)
    for i in range(len(number)):
        if number_check[i] in number:
            if number_check[i] == number[i]:
                bull += 1
            else:
                cow += 1
    return bulls_and_cows.update({'bulls': bull, 'cows': cow})





