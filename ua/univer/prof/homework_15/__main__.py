from ua.univer.prof.homework_15.batmobile import CBatMobile
from ua.univer.prof.lesson_15_vehicles.amfibia import CAmfibia
from ua.univer.prof.lesson_15_vehicles.car import CCar
from ua.univer.prof.lesson_15_vehicles.plane import CPlane
from ua.univer.prof.lesson_15_vehicles.ship import CShip
from ua.univer.prof.lesson_15_vehicles.vehicle_interfaces import ISwim
from ua.univer.prof.lesson_15_vehicles.vehilce import Coord


def is_swimmer(obj):
    return isinstance(obj, ISwim)


def print_swimmer(swim_list):
    for swimmer in swim_list:
        if is_swimmer(swimmer):
            print(swimmer)


def average_price(veh_list):
    total_price, counter = 0, 0
    for v in veh_list:
        total_price += v.price
        counter += 1
    average_price = round(total_price / counter, 2)
    return average_price


def max_speed(veh_list):
    max_speed = veh_list[0]
    for v in veh_list:
        if v.speed > max_speed.speed:
            max_speed = v
    return max_speed


def min_year(veh_list):
    min_year = veh_list[0]
    for v in veh_list:
        if v.year < min_year.year:
            min_year = v
    return min_year


if __name__ == '__main__':
    veh_list = [
        CCar(Coord(1, 1), 10000, 200, 2005),
        CPlane(Coord(10, 10), 100000, 2000, 2015, 300, 40),
        CShip(Coord(2, 2), 500000, 50, 2010, "Odessa", 250),
        CAmfibia(Coord(3, 3), 500000, 50, 2010),
        CBatMobile(Coord(4, 4), 1000000, 200, 2020)
    ]

