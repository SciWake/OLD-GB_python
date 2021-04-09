# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class ZeroExcept(Exception):
    def __init__(self, text):
        self.text = text


class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_result(self):
        if self.b == 0:
            raise ZeroExcept('Ошибка, вы забыли математику')
        return self.a / self.b