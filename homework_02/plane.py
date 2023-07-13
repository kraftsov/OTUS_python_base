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

