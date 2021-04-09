# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def write_date_to_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        while True:
            string = input('Данные для записи: ').strip()
            if len(string) == 0:
                break
            file.write(string + '\n')


def sum_number_to_file(file_name):
    with open(file_name, 'r') as file:
        for string in file.readlines():
            sum = 0
            for number in string.split(' '):
                sum += int(number)
            yield sum, string


if __name__ == '__main__':
    write_date_to_file(input('Ввведите название файла для записи данных: '))
    for sum, string in sum_number_to_file(input('В каком файле произвести подсчёты?')):
        print(f'В строке {string.rstrip()} сумма чисел равна {sum}')
