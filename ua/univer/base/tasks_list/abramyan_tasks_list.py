from ua.univer.base.tasks_list.__main__ import *


def buble_sort(arr):
    n = len(arr)-1
    for x in range(len(arr)):
        for i in range(n):
            if arr[i+1] < arr[i]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
            print(arr)
        n -= 1
    return arr


def simple_sort(arr):
    n = len(arr)-1
    for i in range(len(arr)):
        newarr = []
        for x in arr[0:-i]:
            newarr.append(x)

        print(newarr)
        a = arr.pop(newarr.index(max(newarr)))
        arr.append(a)
    print(arr)


def tasks():
    arr = create_random_massive(12)
    print(arr)
    arr1 = simple_sort(arr)
    print(arr1)
    return arr1


if __name__ == "__main__":
    tasks()