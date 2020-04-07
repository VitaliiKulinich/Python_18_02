from ua.univer.prof.lesson_15_vehicles.vehilce import CVehicle


class CPlane(CVehicle):
    def __init__(self, coord, price, speed, year, height, pass_count):
        CVehicle.__init__(self, coord, price, speed, year)
        self.height = height
        self.pass_count = pass_count

    def __str__(self):
        return f"CPlane {CVehicle.__str__(self)}, {self.height}, {self.pass_count}"

    def print(self):
        print(CPlane.__str__(self))