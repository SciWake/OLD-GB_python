# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))

maximum = 0

while number != 0:
    new_max = number % 10
    number //= 10
    if new_max > maximum:
        maximum = new_max

print(maximum)
