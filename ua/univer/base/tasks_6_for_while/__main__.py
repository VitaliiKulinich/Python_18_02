def first_task():
    for i in range(1, 100, 2):
        print(i)

def second_task(k, n):
    for i in range(n):
        print(k)

def third_task(a, b):
    a = 0
    for i in range(a, b+1):
        print(i)
        a+=1
    print(a)


def fourth_task():
    for i in range(0, -50, -5):
        print(i)


def fiveth_task(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(factorial)


def sixth_task(x, n):
    for i in range(n+1):
        x *= x
    print(x)


def seventh_task_1(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    print(factorial)


def seventh_task_2(x, n):
    while n > 1:
        x *= x
        n -= 1
    print(x)

def eightth_task():
    print("\n", end = " ")
    for i in range(10):
        print("*", end = " ")

    print("\n", end = " ")
    for i in range(3):
        print("*", end = " ")
        for i in range(8):
            print(" ", end = " ")
        print("*", end = " ")
        print("\n", end = " ")

    for i in range(10):
        print("*", end = " ")


def nine_task():
    print("\n", end=" ")
    print("*", end = " ")
    print("\n", end=" ")
    n = 6
    for i in range(n):
        print("*", end = " ")
        for i in range(i):
            print(" ", end = " ")
        print("*", end=" ")
        print("\n", end = " ")
    for i in range(n+2):
        print("*", end=" ")

def tenth_task():
    k = 7
    n = int(( k+1 ) / 2)
    m = int((k // 2) - 1)
    z = 1
    print("\n ", end="")
    for i in range(k//2):
        print("  ", end = "")
    print("* ", end = "")
    for i in range(k//2):
        print("  ", end = "")
    print("\n ",end="")

    for i in range(n-2):
        for i in range(m):
            print("  ", end = "")

        print("* ", end = "")

        for i in range(z):
            print("  ", end = "")

        print("* ", end="")

        for i in range(m):
            print("  ", end = "")
        m -= 1
        z += 2
        print("\n ", end = "")

    for i in range(k):
        print("* ", end="")

def eleventh_task(k):
    if k%2 == 0: k += 1
    n = int(( k+1 ) / 2)
    m = int((k // 2) - 1)
    z = 1

    print("\n ", end="")
    for i in range(k//2):
        print("  ", end = "")
    print("* ", end = "")
    for i in range(k//2):
        print("  ", end = "")
    print("\n ",end="")

    for i in range(n-2):
        for i in range(m):
            print("  ", end = "")

        print("* ", end = "")

        for i in range(z):
            print("  ", end = "")

        print("* ", end="")

        for i in range(m):
            print("  ", end = "")
        m -= 1
        z += 2
        print("\n ", end = "")



    for i in range(n-1):
        for i in range(m):
            print("  ", end = "")

        print("* ", end = "")

        for i in range(z):
            print("  ", end = "")

        print("* ", end="")

        for i in range(m):
            print("  ", end = "")
        m += 1
        z -= 2
        print("\n ", end = "")

    for i in range(k // 2):
        print("  ", end="")
    print("* ", end="")
    for i in range(k // 2):
        print("  ", end="")
    print("\n ", end="")

if __name__ == "__main__":
    eleventh_task(8)