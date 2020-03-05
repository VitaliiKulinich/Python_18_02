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


int
def task1():
    arr = create_random_massive(10)
    print(arr)


if __name__ == "__main__":
    task1()