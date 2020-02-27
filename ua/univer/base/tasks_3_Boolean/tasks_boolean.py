def task_1_boolean():
    a = 1
    if a:
        print("Число а положительное")
    else:
        print("Число а отрицательное")


def task_2_boolean():
    a = 49
    a %= 2
    if a:
        print("Число нечётное")
    else:
        print("Число чётное")


def task_29_boolean():
    x = 2
    y = 3
    x1 = 5
    y1 = 6
    x2 = 1
    y2 = 2
    xmax = max(x1, x2)
    xmin = min(x1, x2)
    ymax = max(y1, y2)
    ymin = min(y1, y2)
    if xmin <= x <= xmax and ymin <= y <= ymax:
        print("The point (X,Y) is inside the rectangle")
    else:
        print("The point (X,Y) is outside the rectangle")


def task_34_boolean():
    x = 1
    y = 2
    z = x + y
    z %= 2
    if z:
        print("White")
    else:
        print("Black")


def task_40_boolean():
    x1 = 1
    y1 = 1
    x2 = 2
    y2 = 3
    ax = abs(x1 - x2)
    ay = abs(y1 - y2)
    if ax == 2 and ay == 1 or ax == 1 and ay == 2:
        print("Кінь може перейти на це поле")
    else:
        print("Кінь не може перейти на це поле")