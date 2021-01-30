# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_int_date(cls, date):
        return list(map(int, date.split('-')))

    @staticmethod
    def valid(day, month, year):
        if day < 1 or day > 31:
            return 'Такой день не существует'
        elif month < 1 or month > 12:
            return 'Такого месяца нет'
        elif year < 0:
            return 'Введите положительный год'

        return f'{day}-{month}-{year}'

    def __str__(self):
        return f'Текущая дата {Date.get_int_date(self.date)}'


t = Date('12-02-2020')
print(t)
# Текущая дата [12, 2, 2020]

print(t.valid(17, 13, 2020))
# Такого месяца нет

print(t.valid(12, 12, 2020))
# 12-12-2020
