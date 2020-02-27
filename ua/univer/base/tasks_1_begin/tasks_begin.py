def perimetr():
    a = int(input("Enter side of the square: "))
    P = 4 * a
    print("Perimeter =", P)


def square():
    a = int(input("Enter side of the square: "))
    S = a ** 2
    print("Square =", S)


def perimetr_square_of_rectangle():
    a = int(input("Enter first side of the rectangle: "))
    b = int(input("Enter second side of the rectangle: "))
    S = a * b
    P = 2 * (a + b)
    print("Square =", S, "\nPerimetr =", P)


def length_of_circle():
    d = int(input("Enter diamert: "))
    pi = 3.14
    L = pi ** 3


def volume_square_of_cube():
    a = int(input("Enter side of cube: "))
    V = a ** 3
    S = 6 * a ** 2
    print("Volume =", V, "\nSquare =", S)


def volume_square_of_rectangular_parallelepiped():
    a = int(input("Enter first side of rectangular parallelepiped: "))
    b = int(input("Enter second side of rectangular parallelepiped: "))
    c = int(input("Enter third side of rectangular parallelepiped: "))
    V = a * b * c
    S = 2 * (a * b + b * c + a * c)
    print("Volume =", V, "\nSquare =", S)


def length_square_of_circle():
    R = int(input("Enter radius: "))
    pi = 3.14
    L = 2 * pi * R
    S = pi * R ** 2
    print("Length =", L, "\nSquare =", S)


def average_value():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = (a + b) / 2
    print("Аverage value =", c)
