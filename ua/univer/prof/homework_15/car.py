from ua.univer.prof.lesson_15_vehicles.vehicle_interfaces import IMove
from ua.univer.prof.lesson_15_vehicles.vehilce import CVehicle


class CCar(CVehicle, IMove):
    def __init__(self, coord, price, speed, year):
        CVehicle.__init__(self, coord, price, speed, year)

    def move(self):
        return self.speed

    def __str__(self):
        return f"CCar {CVehicle.__str__(self)}"

    def print(self):
        print(CCar.__str__(self))
