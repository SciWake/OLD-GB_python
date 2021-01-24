# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
# из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pencil(Stationery):
    @staticmethod
    def draw():
        print('Рисуем карандашом')


class Pen(Stationery):
    @staticmethod
    def draw():
        print('Рисуем ручкой')


class Handle(Stationery):
    @staticmethod
    def draw():
        print('Рисуем маркером')


stat = Stationery
stat.draw()
# Запуск отрисовки

pencil = Pencil
pencil.draw()
# Рисуем карандашом

pen = Pen
pen.draw()
# Рисуем ручкой

handle = Handle
handle.draw()
# Рисуем маркером
