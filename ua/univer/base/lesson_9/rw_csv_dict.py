import csv


def write_dict_to_csv(list_dict_er):
    with open("dict.er", "w") as wfile:
        columns = ["eng", "ru", "ua", "fr"]
        writer = csv.DictWriter(wfile, fieldnames=columns)
        writer.writeheader()
        writer.writerows(list_dict_er)


def read_dict_from_file():
    with open("dict.er", "r") as rfile:
        reader = csv.DictReader(rfile)
        list_dict = []
        for row in reader:
            list_dict.append(dict(row))
        return list_dict



def print_list_of_dict(list_dict):
    for dict_eruf in list_dict:
        print(dict_eruf)

