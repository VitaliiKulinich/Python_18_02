from ua.univer.prof.homework_13.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, coord, price, speed, year):
        super(Car, self).__init__(coord, price, speed, year)

    def __str__(self):
        return f"Car: {self.coord}, {self.price}, {self.speed}, {self.year}"