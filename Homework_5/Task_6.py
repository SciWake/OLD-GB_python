# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for string in file.readlines():
            yield string.strip().replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('.', '').split(' ')


def sum_number(array_numbers):
    sum = 0
    for number in array_numbers:
        try:
            sum += int(number)
        except ValueError:
            continue
    return sum


def main():
    info_dict = {}
    file_name = input('Введите название файла: ')
    for data in read_data(file_name):
        info_dict[data[0]] = sum_number(data[1:])
    return info_dict


print(main())
# {'Информатика:': 170, 'Физика:': 40, 'Физкультура:': 30}
