# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

replace = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for string in file.readlines():
            yield string.strip()


def replace_data(text):
    '''
    Построчная замена, которая выполняется из словаря replace
    :param text: Текст для замены
    :return: Возвращает текс, где произведена замена
    '''
    for number in replace:
        text = text.replace(number, replace[number])
    return text


def main(read_file_name, save_file_name):
    with open(save_file_name, 'w+', encoding='utf-8') as file:
        for string in read_data(read_file_name):  # Построчное чтение данных
            replace_string_data = replace_data(string)  # Обращение к функции для замены
            file.write(replace_string_data + '\n')  # Запись данных в файл


main('Task_4.txt', 'result.txt')
