from ua.univer.prof.lesson_11_market.currency import Currency
from ua.univer.prof.lesson_11_market.product import Product
from ua.univer.prof.lesson_11_market.product_list import Product_List

if __name__ == '__main__':
    Currency.USD = 26.0
    p1 = Product("fruit", "apple", 1, 25)
    p2 = Product("fruit", "banana", 2, 35)
    products = Product_List()
    products.append(p1)
    products.append(p2)
    products.append(Product("technics", "IPhone7", 0.2, 10000))
    products.append(Product("technics", "IPhoneX", 0.25, 20000))

    products.print()
    products.write_to_csv("products.csv")
    products.read_from_csv("products.csv")
    products.print()


    print("\n")
    print(p1)