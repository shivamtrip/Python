from tkinter import *


list = []

def add():
    n1 = number.get()
    list.append(n1)
    e1.insert (END,"+")
    list.append("+")

def multiply():
    n1 = number.get()
    list.append(n1)
    e1.insert (END,"*")
    list.append("*")


def subtract():
    n1 = number.get()
    list.append(n1)
    e1.insert (END,"-")
    list.append("-")

def divide():
    n1 = number.get()
    list.append(n1)
    e1.insert (END,"/")
    list.append("/")


def equal():
    n1 = number.get()
    list.append(n1)
    count = len(list)
    try:
        ans = eval(list[count-1])
    except SyntaxError:
        ans = ""
        list.clear()
    e1.delete(0, END)
    e1.insert(END, ans)


def clear():
    e1.delete(0,END)


def val0():
    e1.insert(END, "0")

def val1():
    e1.insert(END, "1")

def val2():
    e1.insert(END, "2")

def val3():
    e1.insert(END, "3")

def val4():
    e1.insert(END, "4")

def val5():
    e1.insert(END, "5")

def val6():
    e1.insert(END, "6")

def val7():
    e1.insert(END, "7")

def val8():
    e1.insert(END, "8")

def val9():
    e1.insert(END, "9")

def val_dec():
    e1.insert(END, ".")

window = Tk()

number = StringVar()

#e1 = Text(window, width = 20, height = 3)
#e1.insert(number)

e1 = Entry(window, textvariable = number, font=('Ubuntu', 36))
e1.grid(row=0, column = 0, rowspan = 2, columnspan = 4)

b0 = Button(window, text = "0", width = 15, height=5, command=val0, font=('Ubuntu',12))
b0.grid(row=6, column = 0)

b1 = Button(window, text = "1",width = 15, height=5,command=val1, font=('Ubuntu',12))
b1.grid(row=5, column = 0)

b2 = Button(window, text = "2",width = 15,height=5, command=val2, font=('Ubuntu',12))
b2.grid(row=5, column = 1)

b3 = Button(window, text = "3",width = 15,height=5, command=val3, font=('Ubuntu',12))
b3.grid(row=5, column = 2)

b4 = Button(window, text = "4",width = 15,height=5, command=val4, font=('Ubuntu',12))
b4.grid(row=4, column = 0)

b5 = Button(window, text = "5",width = 15, height=5,command=val5, font=('Ubuntu',12))
b5.grid(row=4, column = 1)

b6 = Button(window, text = "6",width = 15,height=5, command=val6, font=('Ubuntu',12))
b6.grid(row=4, column = 2)

b7 = Button(window, text = "7",width = 15,height=5, command=val7, font=('Ubuntu',12))
b7.grid(row=3, column = 0)

b8 = Button(window, text = "8",width = 15,height=5, command=val8, font=('Ubuntu',12))
b8.grid(row=3, column = 1)

b9 = Button(window, text = "9",width = 15,height=5, command=val9, font=('Ubuntu',12))
b9.grid(row=3, column = 2)

b_dec = Button(window, text = ".",width = 15,height=5, command=val_dec, font=('Ubuntu',12))
b_dec.grid(row=6, column = 1)

b_eq = Button(window, text = "=",width = 15,height=5, command = equal, font=('Ubuntu',12))
b_eq.grid(row=6, column = 2)

b_plus = Button(window, text = "+",width = 15,height=5, command = add, font=('Ubuntu',12))
b_plus.grid(row=6, column = 3)

b_minus = Button(window, text = "-",width = 15,height=5, command = subtract, font=('Ubuntu',12))
b_minus.grid(row=5, column = 3)

b_mult = Button(window, text = "x",width = 15, height=5,command = multiply, font=('Ubuntu',12))
b_mult.grid(row=4, column = 3)

b_div = Button(window, text = "/",width = 15,height=5, command = divide, font=('Ubuntu',12))
b_div.grid(row=3, column = 3)

b_clear = Button(window, text="Clear",width = 25, height=5,command=clear, font=('Ubuntu',12))
b_clear.grid(row=7, column=0, columnspan=4)


window.mainloop()
