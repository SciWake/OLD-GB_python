# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for string in file.readlines():
            yield string.strip().split(' ')


if __name__ == '__main__':
    sum = 0
    count_user = 0
    for data in read_data('text.txt'):
        try:
            count_user += 1
            user_salary = int(data.pop())
            sum += user_salary
        except ValueError:
            print('В файл переданы ошибочные данные')
            continue
        if user_salary < 20000:
            print(f'Оклад {data[0]} составляет {user_salary}')

    print(f'Средняя величина дохода {sum / count_user}')
