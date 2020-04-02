from ua.univer.prof.homework_13.vehicle import Vehicle


class Ship(Vehicle):
    def __init__(self, coord, price, speed, year, number_of_passengers, number_port):
        super().__init__(coord, price, speed, year)
        self.number_port = number_port
        self.number_of_passengers = number_of_passengers

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, value):
        self.__number_of_passengers = value

    @property
    def number_port(self):
        return self.__number_port

    @number_port.setter
    def number_port(self, value):
        self.__number_port = value

    def __str__(self):
        return f"Ship: {self.coord}, {self.price}, {self.speed}, {self.year}, {self.number_of_passengers}," \
               f" {self.number_port}"
