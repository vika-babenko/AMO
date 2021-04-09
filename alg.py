import math
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("АМО_Лабораторна робота 4")
root.geometry('480x500')
root["bg"] = "yellow"

a_ent = Entry(root)
b_ent = Entry(root)
ebs_ent = Entry(root)

# похідна
def df(x):
    return 3 * x ** 2 - 1

# функція
def function(x):
    return x**3 - x + 1


# отримуємо а, б, похибку(значення)
def getDots():
    try:
        a = float(a_ent.get())
        b = float(b_ent.get())
        e = float(ebs_ent.get())
        x = np.linspace(a, b, 100)
        y = list(map(function, x))
    except:
        messagebox.showinfo("Error", "Введіть правильні значення!!!")

    return a, b, e, x, y

# графік
def showGraph():
    a, b, e, x, y = getDots()
    if function(a) * function(b) > 0:
        messagebox.showinfo("Error", "Помилкові а, b.\nВведіть інші значення!")
    else:
        x0, y0 = half_divide_method(a, b, e)
        x_0["text"] = "X0 = {}".format(x0)
        f_x0["text"] = "f(x0) = {}".format(y0)

        plt.plot(x, y)
        plt.plot(x0, y0, 'o')

        plt.grid(True)
        plt.show()


# пошук діапазонів коренів рівняння
def find_ranges():
    a = -100
    b = 100
    step = 1
    n = (b-a)/step
    b = a+step
    kranges = []
    for i in range(int(n)):
        fa = function(a)
        fb = function(b)
        if fa*fb < 0:
            kranges.append([a, b])
        a = b
        b = b+step
    return kranges

# метод половинного ділення(алгоритм)
def half_divide_method(a, b, ebs):
    x = (a + b) / 2
    while math.fabs(function(x)) >= ebs:
        x = (a + b) / 2
        a, b = (a, x) if function(a) * function(x) < 0 else (x, b)
        x = (a + b)/ 2
    return (a + b) / 2, function(x)

# промжок кореня
ranges = find_ranges()

# GUI


label_1 = Label(root, text="Лабораторна робота № 4 з АМО \n Група : ІВ-92 \n Бабенко Вікторія", font=('Times New Roman', 18))
label_1.grid(row=0, column=0)
label_1.config(bg="skyblue")

label_2 = Label(root, text="Варіант 1\nМетод половинного ділення", font=('Helvetica', 15))
label_2.config(bg="skyblue")
label_2.grid(row=1, column=0)

task_path = PhotoImage(file="var.png")
task_image = Label(root, image=task_path)
task_image.grid(column=0, row=2)

label_3 = Label(root, text="Введіть значення меж а, b\n для відрізка [a, b]", font=('Helvetica', 15))
label_3.grid(row=3, column=0)
label_3.config(bg="orange")

label_4 = Label(root, text="Значення a",  font=('Helvetica', 18))
label_5 = Label(root, text="Значення b",  font=('Helvetica', 18))
label_6 = Label(root, text="Точність",  font=('Helvetica', 18))
label_4.config(bg="yellow")
label_5.config(bg="yellow")
label_6.config(bg="yellow")

label_4.grid(column=0,row=4)
label_5.grid(column=0,row=5)
label_6.grid(column=0,row=6)

a_ent.grid(column=1, row=4)
b_ent.grid(column=1, row=5)
ebs_ent.grid(column=1, row=6)

a_ent.config(bg="skyblue")
b_ent.config(bg="skyblue")
ebs_ent.config(bg="skyblue")

x_0 = Label(root,text="X0 = ", font=('Times New Roman', 18))
f_x0 = Label(root,text="f(x0) = ", font=('Times New Roman', 18))

x_0.grid(column=0, row=9)
f_x0.grid(column=0, row=10)
x_0.config(bg="orange")
f_x0.config(bg="orange")

solving_range = Label(root, text="Рівняння має корені на проміжку {0}".format(ranges[0]),  font=('Times New Roman', 14))
solving_range.config(bg="yellow")
solving_range.grid(column=0, row=8)

graphic = Button(root, text="Значення \nГрафік", font=('Times New Roman', 18), command=showGraph)
graphic.config(bg="aqua")
graphic.grid(column=0, row=15)
root.mainloop()
sys.exit()