from ua.univer.prof.homework_13.vehicle import Vehicle


class Plane(Vehicle):
    def __init__(self, coord, price, speed, year, number_of_passengers, height):
        super().__init__(coord, price, speed, year)
        self.number_of_passengers = number_of_passengers
        self.height = height

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, value):
        self.__number_of_passengers = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def __str__(self):
        return f"Plane: {self.coord}, {self.price}, {self.speed}, {self.year}, {self.number_of_passengers}, {self.height}"