from ua.univer.prof.lesson_15_vehicles.vehicle_interfaces import ISwim
from ua.univer.prof.lesson_15_vehicles.vehilce import CVehicle


class CShip(CVehicle, ISwim):
    def __init__(self, coord, price, speed, year, port, pass_count):
        CVehicle.__init__(self, coord, price, speed, year)
        self.pass_count = pass_count
        self.port = port

    def swim(self):
        return self.speed

    def __str__(self):
        return f"CShip {super().__str__()}, {self.port}, {self.pass_count}"

    def print(self):
        print(CShip.__str__(self))