# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

# Ввод данных
data = []
while True:
    input_data = input('Для выхода из режима ввода напишите "megastop"\n Введите данные: ')
    if input_data == 'megastop':
        break
    data.append(input_data)
    print(data)

# Рассчёт индексов прохода
len_lst = len(data)
if not len_lst % 2 == 0:
    len_lst -= 1

# Обмен данных
for i in range(0, len_lst, 2):
    a = data[i + 1]
    data[i + 1] = data[i]
    data[i] = a

print(data)
