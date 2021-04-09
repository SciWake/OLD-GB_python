# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex:

    def __init__(self, a, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b >= 0:
            return f'{self.a}+{self.b}j'
        return f'{self.a}{self.b}j'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)


z_1 = Complex(1, 1)
z_2 = Complex(1, 4)

print(z_1 * z_2)
# -3+5j

print(z_1 + z_2)
# 2+5j
