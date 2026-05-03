"""
CLASS ASSOCIATION
A Car object holds references to Engine and Manufacturer objects via properties. Multiple cars can share the same engine and manufacturer instances, illustrating a many-to-one relationship and basic encapsulation with getters/setters.
"""


class Car:
    def __init__(self, name) -> None:
        self.name = name
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    # def display_car_attr(self):
    #     print(self.name, self._engine.name, self.manufacturer.name)


class Engine:
    def __init__(self, name) -> None:
        self.name = name


class Manufacturer:
    def __init__(self, name) -> None:
        self.name = name


car1 = Car("Maverick")
car2 = Car("Mustang")
manufacturer1 = Manufacturer("Ford")
engine1 = Engine("V8")

car1.engine = engine1
car1.manufacturer = manufacturer1

car2.engine = engine1
car2.manufacturer = manufacturer1

# car1.display_car_attr()
# car2.display_car_attr()

print(car1.name, car1.engine.name, car1.manufacturer.name)
print(car2.name, car2.engine.name, car2.manufacturer.name)
