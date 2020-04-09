from tkinter import *


def btn_Ok_click():
    txt.set(message.get())


if __name__ == '__main__':
    win = Tk()
    win.title("First window")
    win.geometry("400x300")
    txt = StringVar()
    message = StringVar()
    txt.set("Hello world!!!")
    btn = Button(win, text="Ok", command=btn_Ok_click)
    lbl = Label(win, textvariable=txt)
    txtfld = Entry(win, textvariable=message)
    lbl.grid(row=0, column=0, sticky="s")
    txtfld.grid(row=0, column=1, sticky="s")
    btn.grid(row=0, column=2, sticky="s")

    win.mainloop()

