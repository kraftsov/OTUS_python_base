"""
Создайте класс `Car`, наследник `Vehicle`
Добавьте атрибут engine классу Car. Объявите метод set_engine,
который принимает в себя экземпляр объекта Engine и устанавливает
на текущий экземпляр Car
"""
from homework_02.engine import Engine
from homework_02.base import Vehicle


class Car(Vehicle):
    engine = None

    def set_engine(self, engine):
        if isinstance(engine, Engine):
            self.engine = engine

# car_zapor = Car()

