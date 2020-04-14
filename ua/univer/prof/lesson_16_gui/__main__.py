from tkinter import *
from tkinter import messagebox

from ua.univer.prof.lesson_13_14_inheritance.human_factory import Human_factory


def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")


def open_file():
    global humans
    humans_factory = Human_factory()
    humans = humans_factory.read_from_csv("humans.csv")

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    humans_listbox = Listbox(root, yscrollcommand=scrollbar.set, width=40)

    for h in humans:
        humans_listbox.insert(END, h.__str__())

    humans_listbox.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=humans_listbox.yview)


def view_info():
    str_info = "Humans: \n"
    for h in humans:
        str_info += h.__str__()
        str_info += "\n"
    messagebox.showinfo("GUI Python", str_info)


if __name__ == '__main__':
    humans = []
    root = Tk()
    root.title("GUI на Python")
    root.geometry("300x250")

    main_menu = Menu()

    file_menu = Menu()
    file_menu.add_command(label="New")
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit")

    main_menu.add_cascade(label="File", menu=file_menu)
    main_menu.add_cascade(label="Edit", command=edit_click)
    main_menu.add_cascade(label="View", command=view_info)

    root.config(menu=main_menu)

    root.mainloop()
