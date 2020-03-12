import csv


def main():
    users = [
        ["Tom", 1234],
        ["Bob", 2345],
        ["Tom", 123443],
        ["Bob", 234542342]

    ]
    filename = "users.csv"
    read_from_csv(filename)

def read_from_csv(filename):
    arr_r = []
    with open(filename, "w", newline="") as users_csv:
        csv_r = csv.reader(users_csv)
        for row in csv_r:
            arr_r.append(row)
    return arr_r

def write_to_csv(filename):
    global users_csv
    with open(filename, "w",newline="") as users_csv:
        csv_w = csv.writer(users_csv)
        csv_w.writerows(users)





if __name__ == '__main__':
    main()