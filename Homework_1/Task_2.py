# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Ввведите количество секунд: '))

hour = seconds // 3600
minutes = (seconds - (3600 * hour)) // 60
seconds -= (hour * 60 + minutes) * 60


print(f'{hour}:{minutes}:{seconds}')


