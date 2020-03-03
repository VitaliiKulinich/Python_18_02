from ua.univer.base.lesson5.__main__ import input_data
from ua.univer.base.lesson5.acount import calculate_complex_rate, calculate_simple_rate


def menu():
    print(" 1 . Calculate complex rate\n 2 . Calculate simple rate")
    option = input("Enter type of rate [1/2] = ")
    money, period, rate = input_data()
    if option == "1":
        result = calculate_complex_rate(rate, money, period)
        return result
    elif option == "2":
        result = calculate_simple_rate(rate, money, period)
        return result

