from ua.univer.prof.homework_15.car import CCar
from ua.univer.prof.homework_15.vehicle_interfaces import IMove, ISwim, IFly


class CBatMobile(CCar, IMove, ISwim, IFly):
    def __init__(self, coord, price, speed, year):
        super().__init__(coord, price, speed, year)

    def __str__(self):
        return f"CBatMobile {self.coord}, {self.price}, {self.speed}, {self.year}"

    def print(self):
        print(self)

    def move(self):
        return self.speed * 2

    def swim(self):
        return self.speed

    def fly(self):
        return self.speed * 5
