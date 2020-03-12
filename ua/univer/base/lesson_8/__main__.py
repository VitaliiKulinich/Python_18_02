import datetime


def main():
    arr = []
    for i in range(5):
        x = validate_mark()
        arr.append(x)
        print(arr)


def validate_mark():
    while True:
        try:
            mark = validate_int_input()
            if mark > 12 or mark < 1:
                raise Exception("Valid is not mark: 0 < mark < 13")
            break
        except Exception as e:
            print(e)
            with open("my.log","a") as log:
                log.write(f"{datetime.datetime.now()} {e} \r")
    return mark


def validate_int_input():
    while True:
        try:
            print("Enter int n position: ")
            x = int(input())
            break
        except Exception as e:
            print("This is not int", str(datetime.datetime.now()))
            with open("my.log","a") as log:
                log.write(f"{datetime.datetime.now()} {e} \r")
    return x


if __name__ == '__main__':
    main()