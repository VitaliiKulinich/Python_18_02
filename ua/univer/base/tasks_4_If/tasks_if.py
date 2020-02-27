def task_1_if():
    x = 165
    if x > 0:
        x += 1

def count_positive_value(x1, x2, x3):
    #x1, x2, x3 = 16, 32, 213
    counter = 0
    if x1 > 0: counter += 1
    if x2 > 0: counter += 1
    if x3 > 0: counter += 1
    print("Positive count {0}".format(counter))

def count_negative_value(x1, x2, x3):
    counter = 0
    if x1 < 0: counter += 1
    if x2 < 0: counter += 1
    if x3 < 0: counter += 1
    print("Negative count {0}".format(counter))

def task_22_if():
    x = -5
    y = -7

    if x > 0 and y > 0:
        print("1")
    elif x > 0 and y < 0:
        print("2")
    elif x < 0 and y < 0:
        print("3")
    else:
        print("4")


def task_26_if():
    x = 1.2
    if x <= 0:
        y = -x

    elif 0 < x < 2:
        y = x ** 2

    elif 2 <= x:
        y = 4

    print(y)


def task_30_if():
    x = 321

    if x % 2:
        y = "Непарне"
    else:
        y = "Парне"

    if x // 100:
        z = "трьохзначне"
    elif x // 10:
        z = "двозначне"
    else:
        z = "однозначне"

    print("{0} {1} число".format(y, z))