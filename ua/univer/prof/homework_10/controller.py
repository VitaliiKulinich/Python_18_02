from ua.univer.prof.homework_10.product import Product


def create_class_and_arr():
    apple_1 = Product("fruit", "apple", 0.5, 23)
    apple_2 = Product("fruit", "apple", 0.3, 30)
    apple_3 = Product("fruit", "apple", 1, 25)
    potato_1 = Product("vegetable", "potato", 20, 17)
    potato_2 = Product("vegetable", "potato", 14, 21)
    phone_1 = Product("appliances", "phone", 0.2, 1000)
    phone_2 = Product("appliances", "phone", 0.25, 1500)
    laptop_1 = Product("appliances", "laptop", 2, 5000)
    laptop_2 = Product("appliances", "laptop", 2.5, 3000)
    laptop_3 = Product("appliances", "laptop", 2.3, 4000)
    arr1 = [
        apple_1, apple_2, apple_3,
        potato_1, potato_2,
        phone_1, phone_2,
        laptop_1, laptop_2, laptop_3
    ]
    return arr1


def task_1(arr):
    arr1 = []
    for i in arr:
        if i.price < 30:
            arr1.append(i)
    product_max_weight = arr1[0]
    for i in arr1:
        if i.weight>product_max_weight.weight:
            product_max_weight = i
    return product_max_weight.name
