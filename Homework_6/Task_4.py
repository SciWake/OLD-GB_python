# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
import random


class Car:
    __status = 'stop'
    __direction = ['Turn right', 'Turn left', 'Moving forward', 'Moving backwards']

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.__status = 'run'
        print(self.__status)

    def stop(self):
        self.__status = 'stop'
        print(self.__status)

    def turn(self):
        print(random.choice(self.__direction))

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    sports_mode = False

    def __init__(self, speed, color, name, is_police, is_spoiler):
        self.is_spoiler = is_spoiler
        Car.__init__(self, speed, color, name, is_police)

    def enabling_sports_mode(self):  # Включение спорт режима
        self.sports_mode = True

    def disabled_sports_mode(self):  # Выключение спорт режима
        self.sports_mode = False


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    flashing_lights = False

    def __init__(self, speed, color, name, is_police, target):
        self.target = target
        Car.__init__(self, speed, color, name, is_police)

    def turning_on_flashing_lights(self):  # Включение проблесковых маячков
        self.flashing_lights = True

    def turning_off_flashing_lights(self):  # Выключение проблесковых маячков
        self.flashing_lights = False


class PoliceSportCar(SportCar, PoliceCar):
    pass


police = PoliceSportCar(speed=290, color='police classic', name='Audi', is_police=True, is_spoiler=True)

police.turning_on_flashing_lights()
print('Статуст проблесковых маячков', police.flashing_lights)
# Статуст проблесковых маячков True

police.enabling_sports_mode()
print('Статуст спортивного режима', police.sports_mode)
# Статуст спортивного режима True

police.show_speed()
# 290
