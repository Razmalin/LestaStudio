import random


# Реализация через двоичное представление данных.
# Четные двоичные числа заканчиваются на 0.
# Для совершения конъюнкции потребуется всего один такт.
def isEven1(value):
    if value & 1 == 0:
        print(value,  " is Even")
    else:
        print(value, " is Odd")


# Реализация через остаток от деления. Никогда не известно, сколько нужно будет раз
# поделить число на два, чтобы узнать остаток.
def isEven2(value):
    if value % 2 == 0:
        print(value, " is Even")
    else:
        print(value, " is Odd")


a = random.randint(0, 1000)
b = random.randint(0, 1000)
isEven1(a)
isEven2(b)
