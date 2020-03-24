import csv

from ua.univer.prof.lesson_11_market.product import Product


class Product_List:
    def __init__(self):
        self.__products = []

    def append(self, product):
        self.__products.append(product)

    def get_total_weight(self):
        sum = 0
        for i in self.__products:
            sum += i.get_weight()
        return sum

    def get_total_price(self):
        sum_price = 0
        for i in self.__products:
            sum_price += i.get_price()
        return sum_price

    def write_to_csv(self, filename):
        with open(filename, "w", newline="") as users_csv:
            csv_w = csv.writer(users_csv)
            for p in self.__products:
                csv_w.writerow(p.list_of_fields())

    def read_from_csv(self, filename):
        self.__products = []
        with open(filename, "r", newline="") as users_csv:
            csv_r = csv.reader(users_csv)
            for row in csv_r:
                type = row[0]
                name = row[1]
                weight = float(row[2])
                price = float(row[3])
                self.__products.append(Product(type, name, weight, price))

    def print_all_apples(self):
        for p in self.__products:
            if p.get_name == "apple":
                print(p.get_name)

    def get_all_apples(self):
        apples = []
        for p in self.__products:
            if p.get_name == "apple":
                apples.append(p)

    def print(self):
        for p in self.__products:
            print(p)