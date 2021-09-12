from random import randint
from termcolor import cprint, colored

global str_wish_number
global bulls


def wishing_number():
    wish_number = randint(1000, 10000)
    global str_wish_number
    str_wish_number = str(wish_number)
    while str_wish_number[0] == str_wish_number[1] or str_wish_number[0] == str_wish_number[2] \
            or str_wish_number[0] == str_wish_number[3] or str_wish_number[1] == str_wish_number[2] or \
            str_wish_number[1] == str_wish_number[3] or str_wish_number[2] == str_wish_number[3]:
        wish_number = randint(1000, 10000)
        str_wish_number = str(wish_number)
    print(wish_number)
    # print(str_wish_number)


def comparing_numbers(user_number):
    cows = 0
    global bulls
    bulls = 0
    for i in range(4):
        if user_number[i] == str_wish_number[i]:
            bulls += 1
        if user_number[i] != str_wish_number[i]:
            if str_wish_number.find(user_number[i]) != -1:
                cows += 1
    result = {'Bulls': bulls, 'Cows': cows}
    cprint(f'Быков {result["Bulls"]}, Коров {result["Cows"]}', color='blue')
    return bulls


def gameover():
    return bulls == 4
