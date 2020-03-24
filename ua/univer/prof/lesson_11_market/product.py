from ua.univer.prof.lesson_11_market.currency import Currency


class Product:
    def __init__(self, type, name, weight, price):
        self.__type = type
        self.__name = name
        self.__weight = weight
        self.set_price(price)

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def set_price(self, price):
        if price > 0:
            self.__price = price/Currency.USD
        else:
            self.__price = 0

    def get_price(self):
        return self.__price*(1.20 + 0.1)*Currency.USD

    def set_weight(self, weight):
        if 0 < weight < 9:
            self.__weight = weight
        else:
            self.__weight = 0
            print("Weight have to be > 0 and < 9")

    def get_weight(self):
        return self.__weight

    def show(self):
        print(f"{self.__type}, {self.__name}, {self.__weight}, {self.__price}")

    def __str__(self):
        return f"{self.__type}, {self.__name}, {self.__weight}, {self.__price}"

    def list_of_fields(self):
        return [self.__type, self.__name, self.__weight, self.__price]