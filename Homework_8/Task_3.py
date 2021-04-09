# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class NotNumberInList(Exception):
    def __init__(self, text):
        self.txt = text


lst = []
while True:
    print('Для выхода введите exit')
    number = input('Введите число: ')

    if number == 'exit':
        break

    try:
        if not number.isdigit():
            raise NotNumberInList('Ошибка ввода')
    except NotNumberInList as e:
        print(e)
        continue
    lst.append(int(number))

print(lst)