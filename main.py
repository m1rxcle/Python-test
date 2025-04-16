# Задание № 1
class Transport(object):

    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Autobus(Transport):
    pass


reno = Autobus("Renaul Logan", 180, 12)

print(
    f"Название автомобиля: {reno.name} Скорость: {reno.max_speed} Пробег: {reno.mileage}"
)


# Задание № 2
class Transport(object):

    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):

        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"


class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


reno = Autobus("Renaul Logan", 180, 12)

print(reno.seating_capacity())
