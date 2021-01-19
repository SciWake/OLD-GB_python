def sum_string():
    for num in input('Введите строку: ').strip().split(' '):
        yield num


def checking_characters(chr):
    if len(chr) > 1:  # В случае, когда символ имеет длину более 1 (например число 10)
        return False
    if ord('!') <= ord(chr) <= ord('/') or ord(chr) in [ord('@'), ord('?'), ord('=')]:  # Проверка спецсимволов
        return True


def main():
    sum = 0
    while True:
        for num in sum_string():
            if checking_characters(num):
                print('Итоговая сумма равна', sum)
                return sum
            sum += int(num)
        print('Итоговая сумма равна', sum)