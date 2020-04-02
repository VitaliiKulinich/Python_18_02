from ua.univer.prof.homework_13.car import Car
from ua.univer.prof.homework_13.plane import Plane
from ua.univer.prof.homework_13.ship import Ship


def max_price_class(vehicles):
    max_price_class = vehicles[0]
    for v in vehicles:
        if v.price > max_price_class.price:
            max_price_class = v
    print(max_price_class)
    return max_price_class


def min_price_class(vehicles):
    min_price_class = vehicles[0]
    for v in vehicles:
        if v.price < min_price_class.price:
            min_price_class = v
    print(min_price_class)
    return min_price_class


if __name__ == '__main__':
    car1 = Car(1, 10000, 200, 2005)
    plane1 = Plane(2, 100000, 600, 2015, 300, 5000)
    ship1 = Ship(3, 1000000, 30, 2019, 500, 123456)
    car2 = Car(4, 120000, 350, 2020)

    vehicles = [car1, plane1, ship1, car2]

