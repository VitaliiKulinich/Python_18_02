from random import *

def task1():
    arr = []
    for i in range(1,20,2):
        arr.append(i)
    print(arr)


def task2():
    arr1 = []
    arr2 = []
    for i in range(10):
        a = input("Enter number:")
        if a % 2:
            arr1.append(a)
        else: arr2.append(a)
    print(arr1, arr2)


def task3():
    arr = [1,3124,4,41,34,431,43]
    x = 0
    y = 0
    for i in arr:
        if i%2: x+=1
        else: y+=1
    print(x,y)


def task4():
    a = 0
    arr = [1,3124,4,41,34,431,43]
    n = len(arr)
    for i in arr:
        a += i
    s = round(a/n, 2)
    print(n, s)


def task5():
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = arr1.copy()
    arr2.reverse()
    for i in range(len(arr1)):
        if i%2 == 0:
            arr1[i] = arr2[i-1]

    print(arr1)
    print(arr2)


def task6():
    arr1 = [1, 2, 1, 4, 1, 6, 7]
    m = min(arr1)
    x = 0
    for i in arr1:
        if m == i:
            print(x)
        x+=1


def task7():
    arr = create_massive(1,10)
    minimal = min(arr)
    maximum = max(arr)
    index_min = arr.index(minimal)
    index_max = arr.index(maximum)
    z = minimal
    arr[index_min] = arr[index_max]
    arr[index_max] = z
    print(arr)


def create_massive1(start = 1, end = 10, step = 1):
    arr = []
    for i in range(start, end, step):
        arr.append(i)
    return arr

def create_random_massive(a):
    arr = []
    for i in range(a):
        arr.append(randint(1,100))
    return arr




