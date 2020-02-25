from ua.univer.base.Function.Functions import count_negative_value, count_positive_value, a


def enter_positive_int():
    y = int(input("Enter int = "))
    if y > 0: return y
    else:
        print("Not positive, your number 0")
        return 0

#if __name__ == "__main__":

    print("hi main")

    x = enter_positive_int()
    y = enter_positive_int()
    z = enter_positive_int()

    count_negative_value(x, y, z)
    count_positive_value(x, y, z)
