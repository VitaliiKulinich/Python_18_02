from abc import ABC, abstractmethod


class Coord:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __str__(self):
        return f"{self.x}, {self.y}"


class CVehicle(ABC):
    def __init__(self, coord, price, speed, year):
        self.year = year
        self.speed = speed
        self.price = price
        self.coord = coord

    def __str__(self):
        return f"{self.coord}, {self.price}, {self.speed}, {self.year}"

    @abstractmethod
    def print(self):
        pass
