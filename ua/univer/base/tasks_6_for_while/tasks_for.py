def task_5():
    price = 12
    for i in range(10):
        a = round((i + 1) * 0.1 * price, 2)
        print("{0}".format(a))


def task_12():
    n = 3
    x = 1
    for i in range(n):
        a = 1 + (i + 1) / 10
        x *= a
    print(round(x, 2))


def task_36():
    n = 4
    k = 3
    x = 1
    for i in range(1, n+1):
        x += float(i**n)
    print(x)


def task_33():
    f = [1, 1]
    n = 9
    for i in range(n-2):
        f.append(f[i]+f[i+1])
    print(f)


def task_20():
    n = 4
    k = 0
    z = 1
    for i in range(1, 1+n):
        z *= i
        k += z
    print(int(k))




