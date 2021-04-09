# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

def count_string_to_file(file_name: str):
    with open(file_name, 'r') as file:
        print(f'В {file_name} содержится {len(file.readlines())} строк')


count_string_to_file('text.txt')
