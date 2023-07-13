"""
1. Создайте класс `Plane`, наследник `Vehicle`.
2. Добавьте атрибуты cargo и max_cargo классу Plane.
3. Добавьте max_cargo в инициализатор (переопределите родительский).
4. Объявите метод load_cargo, который принимает число, проверяет, что в сумме
с текущим cargo не будет перегруза, и обновляет значение.
В ином случае выкидывает исключение exceptions.CargoOverload.
5. Объявите метод remove_all_cargo, который обнуляет значение cargo
и возвращает прежнее. То, которое было до обнуления.
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight: int = 1000, fuel: float = 0, fuel_consumption: float = 10, max_cargo: float = 2000):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        if add_cargo + self.cargo <= self.max_cargo:
            self.cargo = self.cargo + add_cargo
        else:
            raise CargoOverload('Вес груза больше допустимого')

    def remove_all_cargo(self):
        mem = self.cargo
        self.cargo = 0
        return mem

