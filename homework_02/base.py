from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    # добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
    def __init__(self, weight: int = 1000, fuel: float = 0, fuel_consumption: float = 10):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __repr__(self):
        return f'{self.__dict__}'

    def start(self):

        if self.started is False:
            if self.fuel > 0:
                print('Топливо есть еще!')
                self.started = True
            # return self.started
            else:
                raise LowFuelError

    def move(self, distance):
        if distance <= (self.fuel // self.fuel_consumption):
            print(f'Топлива проехать {distance}км хватит')
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel
