# # Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def input_sweets(name):
    x = int(input(f"{name}, введите количество конфет, которые хотите взять от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name} не жульничай, введи другое значение конфет: "))
    return x

def print_way(name, k, counter, value):
    print(f"Ходил {name}, взял {k} конфет(у), у него стало {counter}. На столе осталось {value} конфет(а).")


# Человек против человека

# player1 = input("What is your name?: ")
# player2 = input("What is your name?: ")
# value = int(input("How many sweets will be on the table?: "))
# flag = randint(0, 2)
# if flag:
#     print(f"{player1} get ready!")
# else:
#     print(f"{player2} get ready!")

# counter1 = 0
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_sweets(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         print_way(player1, k, counter1, value)
#     else:
#         k = input_sweets(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         print_way(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл игрок под именем: {player2}")
# else:
#     print(f"Выиграл игрок под именем: {player1}")


"""-------------------------------------------------------------------"""

# Вариант с ботом)

# player1 = input("What is your name?: ")
# player2 = "Bot"
# value = int(input("How many sweets will be on the table?: "))
# flag = randint(0, 2)
# if flag:
#     print(f"{player1} get ready!")
# else:
#     print(f"{player2} get ready!")

# counter1 = 0
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_sweets(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         print_way(player1, k, counter1, value)
#     else:
#         k = randint(1, 29)
#         counter2 += k
#         value -= k
#         flag = True
#         print_way(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл игрок под именем: {player2}")
# else:
#     print(f"Выиграл игрок под именем: {player1}")

"""-------------------------------------------------------------------"""

# Вариант бот c мозгами)

# Первый вариант, тут он не может нормально обыгрывать!

# def bot_calc(value):
#     k = randint(1, 29)
#     while value-k <= 28 and value > 29:
#         k = randint(1, 29)
#     return k

# Второй вариант, тут он хотябы может посоревноваться!

# def bot_calc(value):
#     if value > 56:
#         k = randint(1, 29)
#     else:
#         k = 28
#     return k

# player1 = input("What is your name?: ")
# player2 = "Bot"
# value = int(input("How many sweets will be on the table?: "))
# flag = randint(0, 2)
# if flag:
#     print(f"{player1} get ready!")
# else:
#     print(f"{player2} get ready!")

# counter1 = 0
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_sweets(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         print_way(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         print_way(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл игрок под именем: {player2}")
# else:
#     print(f"Выиграл игрок под именем: {player1}")

"""-------------------------------------------------------------------"""

# Попробуй обыграть бота! С какой попытки получилось?

def bot_calc(value):
    if value > 114:
        k = randint(1,29)
    elif value >= 86:
        k = value - 85
    elif value >= 59:
        k = value - 58
    elif value == 58:
        k = 28
    elif value >= 30:
        k = value - 29
    elif value == 29:
        k = randint(1,29)
    else:
        k = value
    return k

player1 = input("What is your name?: ")
player2 = "Bot"
value = int(input("How many sweets will be on the table?: "))
flag = randint(0, 2)
if flag:
    print(f"{player1} get ready!")
else:
    print(f"{player2} get ready!")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_sweets(player1)
        counter1 += k
        value -= k
        flag = False
        print_way(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        print_way(player2, k, counter2, value)

if flag:
    print(f" {player1} поздравляю! Ты сделал это, забрал последнюю(ие) конфету(ы) и победил Конфетного Бота")
else:
    print(f" Ты проиграл:( {player2} забирает последнюю(ие) конфету(ы) и выигрывает!")