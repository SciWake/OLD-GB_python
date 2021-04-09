# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

class Clothes:
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @property
    def get_info(self):
        if self.name.lower() == 'пальто':
            return round(self.param / 6.5 + 0.5, 3)
        elif self.name.lower() == 'костюм':
            return round(self.param * 2 + 0.3, 3)
        else:
            return f'Неизвестный тип одежды {self.name}'


coat = Clothes(name='Пальто', param=8)
print(coat.get_info)

suit = Clothes(name='Костюм', param=180)
print(suit.get_info)

