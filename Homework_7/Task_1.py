# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


from prettytable import PrettyTable


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = PrettyTable()

        for string_matrix in self.matrix:
            result.add_row(string_matrix)
        return f'{result}'

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return 'Матрицы имеют разный размер'

        result = self.matrix.copy()
        for i in range(len(self.matrix)):

            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix(result)


a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[2, 2, 2], [9, 1, 4]])
print(a)
# +---------+---------+---------+
# | Field 1 | Field 2 | Field 3 |
# +---------+---------+---------+
# |    1    |    2    |    3    |
# |    4    |    5    |    6    |
# +---------+---------+---------+

print(a + b)
# +---------+---------+---------+
# | Field 1 | Field 2 | Field 3 |
# +---------+---------+---------+
# |    3    |    4    |    5    |
# |    13   |    6    |    10   |
# +---------+---------+---------+
