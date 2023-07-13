"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    # print('Это исключение LowFuelError')
    pass


class NotEnoughFuel(Exception):
    pass


class CargoOverload(Exception):
    pass
