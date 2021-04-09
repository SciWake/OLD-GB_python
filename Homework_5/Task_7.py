# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json


def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for string in file.readlines():
            yield string.strip().replace('.', '').split(' ')


def profit(array):
    return array[0] - array[1]


def save_data_to_json(data, file_name):
    with open(file_name + ".json", "w") as write_file:
        json.dump(data, write_file)


def main():
    average_profit = 0  # Средняя прибыль всех фирм
    data_firms = []  # Итоговый массив данных
    firm_info = {}  # Данные по каждой фирме
    file_name = input('Введите название файла: ')

    for string_array in read_data(file_name):  # Получение строки из файла в виде разбитого массива

        int_array = [int(number) for number in string_array[2:]]  # Преобразование строковых данных
        profit_firma = profit(int_array)
        firm_info[string_array[0]] = profit_firma  # Формирвоание словаря с информацией о фирмах

        if profit_firma > 0:
            average_profit += profit_firma

    data_firms.append(firm_info)
    data_firms.append({'average_profit': average_profit / len(firm_info)})

    save_file_name = input('Рассчёты произведены успешно, укажите название файла для сохранения данных: ')
    save_data_to_json(data_firms, save_file_name)  # Сохранение данных


main()
