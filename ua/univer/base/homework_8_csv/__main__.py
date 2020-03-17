import csv


def main():
    file = "zp-lupen-2019.csv"
    with open(file, "r", encoding='cp1251', newline="")as zp_lupen:
        info = csv.reader(zp_lupen)
        info_list, info_list_2 = [], []
        for row in info:
            info_list.append(row)
        print(info_list)
        n = 0

        for i in info_list:
            info_list[n][0] = info_list[n][0].split(",")
            n += 1
        print(info_list)
        for i in range(len(info_list)):
            info_list_2.append(info_list[i][0])
            info_list_2 = info_list_2[i][0].split(";")
        print(info_list_2)

def test_func():
    file = "csv_file_test.csv"
    info = [
        ["Tom; 12; Kiev"],
        ["Bob; 42; Moskov"],
        ["Henry; 23; Berlin"]
    ]
    with open(file,"w", newline="")as file_csv:
        writer = csv.writer(file_csv)
        writer.writerows(info)

    info_list = []
    with open(file, "r", newline="") as file_csv:
        writer = csv.reader(file_csv)
        for row in writer:
            info_list.append(row)
        print(info_list,"\n")
    for i in range(len(info_list)):
        info_list[i] = info_list[i][0].split(";")
    for i in range(len(info_list)):
        if int(info_list[i][1]) > 12:
            print(info_list[i])




if __name__ == '__main__':
    main()
