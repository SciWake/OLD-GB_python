# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, id, city):
        self.id = id
        self.city = city


class OfficeEquipment:
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, weight, price, number_of_pages_per_minute):
        self.number_of_pages_per_minute = number_of_pages_per_minute
        OfficeEquipment.__init__(self, weight, price)


class Scanner(OfficeEquipment):
    def __init__(self, weight, price, image_quality):
        self.image_quality = image_quality
        OfficeEquipment.__init__(self, weight, price)


class CopyShop(OfficeEquipment):
    def __init__(self, weight, price, number_of_transactions):
        self.number_of_transactions = number_of_transactions
        OfficeEquipment.__init__(self, weight, price)
