class Vehicle:
    def __init__(self, coord, price, speed, year):
        self.year = year
        self.speed = speed
        self.price = price
        self.coord = coord

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value >= 2000:
            self.__year = value
        else:
            print("Error year")
            self.__year = 2000

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, value):
        self.__coord = value


