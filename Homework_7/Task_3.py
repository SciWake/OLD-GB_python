# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно.

class Cell:

    def __init__(self, count_cell):
        self.count_cell = count_cell

    def __add__(self, other):
        self.count_cell += other.count_cell

    def __sub__(self, other):
        if self.count_cell > other.count_cell:
            self.count_cell -= other.count_cell
        else:
            print(f'Первая бактерия оказалась меньше второй')

    def __mul__(self, other):
        return Cell(self.count_cell * other.count_cell)

    def __str__(self):
        return f'Бактреия имеет {self.count_cell} ячеек'

    def __truediv__(self, other):
        return Cell(self.count_cell // other.count_cell)

    def make_order(self):
        for i in range(self.count_cell):
            if i % 5 == 0:
                print()
            print('*', end='')


escherichia_coli = Cell(12)
print(escherichia_coli)
# Бактреия имеет 12 ячеек

staphylococcus = Cell(29)

staphylococcus + escherichia_coli
print(staphylococcus)
# Бактреия имеет 41 ячеек

clostridium_botulinum = staphylococcus * escherichia_coli
print(clostridium_botulinum)
# Бактреия имеет 492 ячеек

escherichia_coli_2 = clostridium_botulinum / staphylococcus
print(escherichia_coli_2)
# Бактреия имеет 12 ячеек

escherichia_coli_2.make_order()
# *****
# *****
# **
