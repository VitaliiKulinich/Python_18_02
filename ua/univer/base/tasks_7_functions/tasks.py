def square_perimetr_of_equilateral_triangle():
    a = int(input("Enter length of side: "))
    s = round(a**2 * 3**(1/2) /4, 2)
    p = round(a ** 3, 2)
    print(s, p)
    return s, p


def add_right_digit(k,d):
    z = int(str(k)+str(d))
    print(z)
    return z


def min_max(a,b):
    x = min(a,b)
    y = max(a,b)
    print(x, y)
    return x, y


def sort_numbers(*a):
    a = a.sort()
    print(a)
    return a


def sign(x):
    if x < 0:
        print("-1")
        return -1
    elif x == 0:
        print("0")
        return 0
    elif x > 0:
        print("1")
        return 1


def ring_s():
    r1 = int(input("Enter r1 = "))
    r2 = int(input("Enter r2 = "))
    pi = 3.14
    s1 = r1**2 * pi
    s2 = r2**2 * pi
    s3 = round(s2 - s1, 2)
    print(s3)
    return s3


def degree():
    a = int(input("Enter a ="))
    n = int(input("Enter n ="))
    if n > 0:
        z = a**n
    elif n < 0:
        z = 1/a**abs(n)
    elif n == 0:
        z = 0
    print(z)
    return z


def factorial_2(x, n):
    z = 0
    if n%2:
        for i in range(1, n+1, 2):
            z += i
    else:
        for i in range(2, n+1, 2):
            z += i
    print(z)
    return z


def palindrom(x):
    z = 0
    for i in range(0, len(x)):
        if x[i] == x[:i]:
            z += 1
    if z == len(x):
        print(True)
        return True
    else:
        print(False)
        return False