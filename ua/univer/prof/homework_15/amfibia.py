from ua.univer.prof.lesson_15_vehicles.car import CCar
from ua.univer.prof.lesson_15_vehicles.vehicle_interfaces import IMove, ISwim


class CAmfibia(CCar, IMove, ISwim):
    def __init__(self, coord, price, speed, year):
        super().__init__(coord, price, speed, year)

    def __str__(self):
        return f"CAmfibia {CCar.__str__(self)}"

    def print(self):
        print(self)

    def move(self):
        return self.speed / 2

    def swim(self):
        return self.speed / 3
