def main():
    arr = [1, 2, 3, 134, 532, 523, 31]

    with open("text_file.txt", "r") as file:
        lines = []
        for i in range(len(arr)):
            lines.append(file.readline())
        lines = lines[:-2]
        print(lines)

        lines2 = []
        for i in lines:
            lines2.append(i.split(";"))
        print(lines2)

        lines3 = []
        for row in lines2:
            lines3.append(row[0:2])
        print(lines3)







def matrix_example_change():
    users = (
        ["Tom", 32, "+380671112222"],
        ["Bob", 32, "+380671112222"],
        ["Alice", 19, "+380671112222"]
    )
    users[1][1] = "beer"
    for user in users:
        if user[1] > 20:
            print(user)


def matrix_example():
    users = [
        [11, 12, 13],
        [22, 23, 24]
    ]
    for i in range(2):
        for j in range(3):
            print(users[i][j])


def sort_example():
    arr = [324, 234, 54, 12, 53, 215, 5436, 14314, 12, 32, 241]
    print(arr)
    sort_arr = sorted(arr)
    print(arr)
    print(sort_arr)


if __name__ == '__main__':
    main()
