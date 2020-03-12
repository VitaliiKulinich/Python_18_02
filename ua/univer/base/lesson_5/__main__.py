from ua.univer.base.lesson_5.acount import *
from ua.univer.base.lesson_5.menu import *


def input_data():
    choise = "y"
    while choise == "y":
        rate = int(input("Введите процентную ставку: "))
        money = int(input("Введите сумму: "))
        period = int(input("Введите период ведения счета в месяцах: "))
        choise = (input("Again [y/n]? ")).lower()
    return rate, money, period

def main():
      choise = "y"
      while choise == "y":
            result = menu()
            choise = (input("Again [y/n]? ")).lower()
      return print(result)

if __name__ == "__main__":
    main()
