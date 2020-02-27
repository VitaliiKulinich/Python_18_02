def task_1_integer():
    a = 54774
    a //= 100
    print("M = {0}".format(a))

def task_2_integer():
    a = 54774
    a //= 1000
    print("M = {0}".format(a))


def task_28_integer():
    # день в році (від 1 до 365)
    k = 9
    # день тижня з якого почався рік (від 1 до 7)
    n = 5
    # день тижня знайдений остачою від ділення на 7 числа k (від 0 до 6)
    x = k % 7
    if x == 0: x = 7
    # день тижня з врахуванням здвигу на початку року (від 0 до 6)
    a = (x + n - 1) % 7
    if a == 0: a = 7

    print(x, a)


def task_29_integer():
    # Variables
    a = 7
    b = 4
    c = 2

    # Quality of squares
    q_a = a // c
    q_b = b // c
    q = q_a * q_b
    print("Quality of squares = {0}".format(q))

    # Square of free space
    sq_a = a % c
    sq_b = b % c
    s = sq_a * b + sq_b * a - sq_a * sq_b
    print("Square of free space = {0}".format(s))


def task_30_integer():
    y = 101
    y -= 1
    x = y // 100 + 1
    print(x)
