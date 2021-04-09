# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class PriceType(Exception):  # Проверка на цену
    def __init__(self, text):
        self.txt = text


class WeightType(Exception):  # Проверка на вес
    def __init__(self, text):
        self.txt = text


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
        self.validate(price=price, weight=weight)  # Выполняем проверку
        self.weight = weight
        self.price = price
        self.name = name

    @staticmethod
    def validate(price, weight):
        '''
        Функция проверки параметров
        :param price: Цена товара
        :param weight: Вес товара
        '''
        if not type(price) in [int, float] or price < 0:
            raise PriceType('Должно быть положительное число')
        if not type(weight) in [int, float] or weight < 0:
            raise WeightType('Должно быть положительное число')


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
kseonum_03_2 = Printer(name='kseonum_03_2', weight='2.5', price=17780, number_of_pages_per_minute=90)
