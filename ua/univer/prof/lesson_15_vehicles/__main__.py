from ua.univer.prof.lesson_15_vehicles.amfibia import CAmfibia
from ua.univer.prof.lesson_15_vehicles.car import CCar
from ua.univer.prof.lesson_15_vehicles.dog import Dog
from ua.univer.prof.lesson_15_vehicles.plane import CPlane
from ua.univer.prof.lesson_15_vehicles.ship import CShip
from ua.univer.prof.lesson_15_vehicles.vehicle_interfaces import IMove, ISwim
from ua.univer.prof.lesson_15_vehicles.vehilce import Coord


def is_swimmer(obj):
    return isinstance(obj, ISwim)


def print_swimmer(swim_list):
    for swimmer in swim_list:
        if is_swimmer(swimmer):
            print(swimmer.swim())


if __name__ == '__main__':
    veh_list = [
        CCar(Coord(1, 1), 10000, 200, 2005),
        CPlane(Coord(10, 10), 100000, 2000, 2015, 300, 40),
        CShip(Coord(2, 2), 500000, 50, 2010, "Odessa", 250),
        CAmfibia(Coord(3, 3), 500000, 50, 2010),

    ]
    swim_list = []
    for v in veh_list:
        if isinstance(v, ISwim):
            swim_list.append(v)
    swim_list.append(Dog())

    print_swimmer(swim_list)
