import csv

from ua.univer.base.lesson_9.list_dict_controll import *
from ua.univer.base.lesson_9.rw_csv_dict import *



def main_menu():
    global key
    print("Menu:")
    print("1. Read Dictionary from file")
    print("2. Write Dictionary to file")
    print("3. Find translate of word")
    print("4. Add new Word and Translate")
    print("5. Print Dictionary")
    print("0. Exit")
    key = int(input("Enter key: "))
    return key


if __name__ == '__main__':
    list_dict = []
    while True:
        key = main_menu()
        if key == 0:
            break
        elif key == 1:
            list_dict = read_dict_from_file()
        elif key == 2:
            write_dict_to_csv(list_dict)
        elif key == 3:
            find_or_add(list_dict)
        elif key == 4:
            add_word(list_dict)
        elif key == 5:
            print_list_of_dict(list_dict)