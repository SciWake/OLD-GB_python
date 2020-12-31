# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов

def my_func(a, b, c):
    if a > b:
        if c > b:
            return a + c
        else:
            return a + b
    elif c > a:
        return b + c
    else:
        return b + a

