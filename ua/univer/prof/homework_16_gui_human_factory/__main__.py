from tkinter import Tk, Button, StringVar, Entry

from ua.univer.prof.lesson_13_14_inheritance.doctor import Doctor
from ua.univer.prof.lesson_13_14_inheritance.fighter import Fighter
from ua.univer.prof.lesson_13_14_inheritance.human_factory import Human_factory
from ua.univer.prof.lesson_13_14_inheritance.student import Student


def print_list_of_human_type(humans, human_type):
    count_h = 0
    list_h = []
    for h in humans:
        if isinstance(h, human_type):
            count_h += 1
            list_h.append(h)
    print(human_type.__name__, "count find =", count_h)
    for h in list_h:
        if h != None:
            print(h)


def find_human(human_str):
    human_type = humans_factory.get_human_type_by_str(human_str)
    if human_type != None:
        return print_list_of_human_type(humans, human_type)
    else:
        print("No such people")


def menu():
    print("Human Factory:")
    print("1 = Read humans from csv file")
    print("2 = Write humans to csv file")
    print("3 = Print all peoples")
    print("4 = Find a people by name")
    print("0 = Close program")
    key = int(input("Enter key: "))
    return key


def click_button1():
    global humans
    humans = humans_factory.read_from_csv("humans.csv")


def click_button2():
    humans_factory.write_to_csv(humans, "humans.csv")


def click_button3():
    for h in humans:
        print(h)


def click_button4(human):
    find_human(human)


if __name__ == '__main__':
    humans_factory = Human_factory()
    humans = []
    root = Tk()
    root.title("Humans Factory")
    # root.geometry("500x500+100+150")

    message = StringVar()
    message_entry = Entry(textvariable=message)
    btn1 = Button(text="Read humans from csv file", background="#555", foreground="#ccc",
                  padx="100", pady="8", font="16", command=click_button1)
    btn2 = Button(text="Write humans to csv file", background="#555", foreground="#ccc",
                  padx="110", pady="8", font="16", command=click_button2)
    btn3 = Button(text="Print all peoples", background="#555", foreground="#ccc",
                  padx="143", pady="8", font="16", command=click_button3)
    btn4 = Button(text="Find a people by name", background="#555", foreground="#ccc",
                  padx="115", pady="8", font="16", command=click_button4(message.get))

    btn1.grid(row=0, column=0, ipadx=5, ipady=5)
    btn2.grid(row=1, column=0, ipadx=5, ipady=5)
    btn3.grid(row=2, column=0, ipadx=5, ipady=5)
    btn4.grid(row=3, column=0, ipadx=5, ipady=5)
    message_entry.grid(row=4, column=0, ipadx=5, ipady=5)

    root.mainloop()
'''
    while True:
        key = menu()
        if key == 1:
            humans = humans_factory.read_from_csv("humans.csv")
        if key == 2:
            humans_factory.write_to_csv(humans, "humans.csv")
        if key == 3:
            for h in humans:
                print(h)
        if key == 4:
            find_human(humans)
        if key == 0:
            break
'''
