# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


class Warehouse:
    data = {}

    def __init__(self, id, city):
        self.id = id
        self.city = city

    def adding_to_warehouse(self, *items):
        '''
        Заполнение склада

        Данный метод добавлят все параметры созданных объектов
        :param items: Объекты
        '''
        for item in items:
            self.data[item.__class__] = item.__dict__

    def __str__(self):
        return f'Количество вещей на складе {len(self.data)}'

    def get_data(self):
        return self.data


class OfficeEquipment:
    def __init__(self, weight, price, name):
        self.weight = weight
        self.price = price
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, weight, price, number_of_pages_per_minute, name):
        self.number_of_pages_per_minute = number_of_pages_per_minute
        OfficeEquipment.__init__(self, weight, price, name)


class Scanner(OfficeEquipment):
    def __init__(self, weight, price, image_quality, name):
        self.image_quality = image_quality
        OfficeEquipment.__init__(self, weight, price, name)


class CopyShop(OfficeEquipment):
    def __init__(self, weight, price, number_of_transactions, name):
        self.number_of_transactions = number_of_transactions  # Количество возможностей
        OfficeEquipment.__init__(self, weight, price, name)


# Создание склада
sclad_1 = Warehouse(id=1, city='Moscow')


# Создаие предметов
kseonum_03_2 = Printer(name='kseonum_03_2', weight=2.5, price=17780, number_of_pages_per_minute=90)
kaputiun_001 = Printer(name='kaputiun_001', weight=5.4, price=1780, number_of_pages_per_minute=10)

optimum = Scanner(name='optium', weight=1.1, price=14300, image_quality='1920:1080')

scantrum = CopyShop(name='scanrum', weight=12.5, price=43000, number_of_transactions=12)


# Добавление предметов на склад
sclad_1.adding_to_warehouse(kaputiun_001, kseonum_03_2, optimum, scantrum)


# Пример работы
print(sclad_1)
# Количество вещей на складе 4

print(sclad_1.get_data())
# [{'type': <class '__main__.Printer'>, 'info': {'number_of_pages_per_minute': 10, 'weight': 5.4, 'price': 1780...
