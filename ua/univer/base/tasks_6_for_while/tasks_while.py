def task_1():
    a = 13
    b = 2
    i = 1
    while i * b < a:
        i += 1
    print(i - 1)


def task_4():
    r = 1
    s = 3
    n = 9
    while r * s < n:
        r *= s
    if r * s == n:
        print("True")
    else:
        print("False")


def task_7():
    n = 8
    k = 1
    while k**2 < n:
        k += 1
    print("{0}**2 = {1} > {2}".format(k, k**2, n))


def task_12():
    k, n, suma = 1, 16, 1
    while suma <= n:
        k += 1
        suma += k
        if (suma + k) > n:
            break
    print(k, suma)


def task_23():
    a = 10
    b = 6
    while a != 0 and b != 0:
        if a == b:
            return print(a)
        if a > b:
            a = a % b
        elif a < b:
            b = b % a
    if a != 0:
        print(a)
    else:
        print(b)
