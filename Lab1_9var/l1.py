import subprocess
from tkinter import *
from tkinter import messagebox
import math
import file1 as f1
import file2 as f2
import file3 as f3

root = Tk()
root.title("АМО_Лабораторна робота 1")
root.geometry('300x200')
root["bg"] = "navajo white"

def lin_a():
    win1 = Toplevel(root)
    win1["bg"] = "navajo white"
    global task1_path

    def result1():
        try:
            a = float(ent_a.get())
            b = float(ent_b.get())
            c = float(ent_c.get())


        except:
            messagebox.showinfo("Помилка", "Перевірте коректність введених данних")

        try:
            y1_r = (5 + c * math.sqrt(b + 5 * math.sqrt(a))) ** (1 / 3)
            y1["text"] = "Y1 = {}".format(y1_r)
        except:
            messagebox.showinfo("Помилка", "Введіть коректні значення!!!")

    def openFileForEditing():
        subprocess.call(["notepad.exe", "file1.py"])

    def result1_2():
        try:
            a = f1.a
            b = f1.b
            c = f1.c
        except:
            messagebox.showinfo("Помилка", "Дані введені некоректно або не введені!")
        try:
            y1_r = (5 + c * math.sqrt(b + 5 * math.sqrt(a))) ** (1 / 3)
            y1["text"] = "Y1 = {}".format(y1_r)
        except:
            messagebox.showinfo("Помилка", "Не можливо обчислити!")

    name_task = Label(win1, text="Лінійний алгоритм")
    name_task.config(bg="navajo white")

    ent_a = Entry(win1)
    ent_b = Entry(win1)
    ent_c = Entry(win1)


    write_a = Label(win1, text="Значення а")
    write_a.config(bg="pink")
    write_b = Label(win1, text="Значення b")
    write_b.config(bg="pink")
    write_c = Label(win1, text="Значення с")
    write_c.config(bg="pink")
    label_task_name = Label(win1, text="Формула")
    label_task_name.config(bg="pink")
    image_for_task = Label(win1, image=task1_path)

    re_button_1 = Button(win1, text="Розрахувати результат\n Зчитування даних",
                         command=result1)
    ed_file_1 = Button(win1, text="Внести значення \n у файл",
                       command=openFileForEditing)
    re_button_2 = Button(win1, text="Розрахувати результат\n Зчитування даних\n з файлу", command=result1_2)

    y1 = Label(win1, text="\nY1 = \n")
    y1.config(bg="pink")
    name_task.grid(column=0, row=0)
    label_task_name.grid(column=0, row=1)
    image_for_task.grid(column=0, row=2)
    write_a.grid(column=0, row=5)
    write_b.grid(column=0, row=6)
    write_c.grid(column=0, row=7)
    ent_a.grid(column=1, row=5)
    ent_b.grid(column=1, row=6)
    ent_c.grid(column=1, row=7)
    re_button_1.grid(column=0, row=8)
    ed_file_1.grid(column=0, row=10)
    re_button_2.grid(column=1, row=10)
    y1.grid(column=0, row=11)

def branch_algor():
    win2 = Toplevel(root)
    win2.config(bg="navajo white")
    global task2_path
    def r_1():
        try:
            d = float(entry_d.get())
            k = float(entry_k.get())
        except:
            messagebox.showinfo("Error", "Перевірте коректність введених данних")

        try:
            if k > 10:
                y = math.sqrt(k * math.sqrt(d ** 2) + d * math.sqrt(k ** 2))
            else:
                y = (k + d) ** 2
            y1["text"] = "Y1 = {}".format(y)
        except:
            messagebox.showinfo("Помилка", "Введіть коректні значення!!!")


    def result1_2():
        try:
            k = f2.k
            d = f2.d
        except:
            messagebox.showinfo("Помилка", "Дані введені некоректно або не введені!")
        try:
            if k > 10:
                y = math.sqrt(k * math.sqrt(d ** 2) + d * math.sqrt(k ** 2))
            else:
                y = (k + d) ** 2
            y1["text"] = "Y1 = {}".format(y)
        except:
            messagebox.showinfo("Помилка", "Не можливо обчислити!")

    def edit_2():
        subprocess.call(["notepad.exe", "file2.py"])

    task_2 = Label(win2, text="Розгалужений алгоритм")
    task_2.grid(column=0, row=0)
    task_2.config(bg="navajo white")
    name_2 = Label(win2, text="Формула")
    name_2.grid(column=0, row=1)
    name_2.config(bg="pink")
    task_2_im = Label(win2, image=task2_path)
    task_2_im.grid(column=0, row=2)

    label_k = Label(win2, text="Введіть k")
    label_k.config(bg="pink")
    label_d = Label(win2, text="Введіть d")
    label_d.config(bg="pink")
    entry_k = Entry(win2)
    entry_d = Entry(win2)
    label_k.grid(column=0, row=4)
    label_d.grid(column=0, row=5)
    entry_k.grid(column=1, row=4)
    entry_d.grid(column=1, row=5)

    res_1_but = Button(win2, text="Результат за\n введеними даними", command=r_1)
    res_1_but.grid(column=0, row=7)

    res_2_but = Button(win2, text="Змінити данні", command=edit_2)
    res_2_but.grid(column=0, row=8)

    res_22_but = Button(win2, text="Результат за\n даними з файлу")
    res_22_but.grid(column=1, row=8)

    y1 = Label(win2, text="Y1 = ")
    y1.config(bg="pink")
    y1.grid(column=0, row=10)

def cycle_alg():
    global task3_path
    win3 = Toplevel(root)
    win3.config(bg="navajo white")


    def result_of_3_1():
        try:
            list_a = (entry_a.get()).split()
            list_b = (entry_b.get()).split()

            for i in range(len(list_a)):
                list_a[i] = float(list_a[i])
                list_b[i] = float(list_b[i])
        except:
            messagebox.showinfo("Error", "Введено некоректні значення!")

        try:

            res_1 = 1
            res_2 = 0
            for i in range(len(list_a) - 1):
                res_1 *= list_a[i] + list_b[i + 1]
                res_2 += list_a[i + 1] * list_b[i]
            f = res_1 + res_2
            res_3["text"] = "\n\nf = {}".format(f)
        except:
            messagebox.showinfo("Error", "Обчислення не можливі!!!")


    def result_of_3_2():
        try:
            list_a = f3.a
            list_b = f3.b

            for i in range(len(list_a)):
                list_a[i] = float(list_a[i])
                list_b[i] = float(list_b[i])

        except:
            messagebox.showinfo("Error", "Введено некоректні значення!")

        try:
            res_1 = 1
            res_2 = 0
            for i in range(len(list_a) - 1):
                res_1 *= list_a[i] + list_b[i + 1]
                res_2 += list_a[i + 1] * list_b[i]
            f = res_1 + res_2
            res_3["text"] = "\nf = {}".format(f)

        except:
                messagebox.showinfo("Error", "Обчислення не можливі!!!")

    def edit_f3():
        subprocess.call(["notepad.exe", "file3.py"])

    task3 = Label(win3, text="Циклічний алгоритм")
    task3.config(bg="navajo white")
    task3.grid(column=0, row=0)
    task3_image = Label(win3, image=task3_path)
    task3_image.grid(column=0, row=1)

    label_a = Label(win3, text="Введіть значення а")
    label_a.config(bg="pink")
    label_b = Label(win3, text="Введіть значення а")
    label_b.config(bg="pink")

    entry_a = Entry(win3)
    entry_b = Entry(win3)



    label_a.grid(column=0, row=3)
    label_b.grid(column=0, row=5)


    entry_a.grid(column=0, row=4)
    entry_b.grid(column=0, row=6)

    button_1 = Button(win3, text="Зчитати данні\n Результат", command=result_of_3_1)

    button_2 = Button(win3, text="Редагувати файл", command=edit_f3)

    button_3 = Button(win3, text="Зчитати данні з файлу\n Результат", command=result_of_3_2)

    button_1.grid(column=0, row=11)
    button_2.grid(column=0, row=12)
    button_3.grid(column=1, row=12)

    res_3 = Label(win3, text="\nf = \n")
    res_3.config(bg="pink")
    res_3.grid(column=0, row=13)


task1_path = PhotoImage(file="t_1.png")
task2_path = PhotoImage(file="t_2.png")
task3_path = PhotoImage(file="t_3.png")

mainMenu = Menu(root)
root.config(menu=mainMenu)

l1 = Menu(mainMenu, tearoff=0)
l1.add_command(label="Лінійний алгоритм", command=lin_a)
l1.add_command(label="Розгалужений алгоритм", command=branch_algor)
l1.add_command(label="Циклічний алгоритм", command=cycle_alg)

mainMenu.add_cascade(label="Меню", menu=l1)
someAboutUsing = Label(root, text="Для того, щоб переглянути роботу\n використовуйте меню", font=('Arial', 14))
someAboutUsing.config(bg="navajo white")
dataAboutStudent = Label(root, text="Виконала:")
dataAboutStudent.config(bg="navajo white")
name = Label(root, text="Дяченко Віта Юріївна")
name.config(bg="navajo white")
group = Label(root, text="IO-93, ФІОТ")
group.config(bg="navajo white")
variant = Label(root, text="Варіант - 9")
variant.config(bg="navajo white")
someAboutUsing.grid(column=0, row=0)
dataAboutStudent.grid(column=0, row=1)
name.grid(column=0, row=2)
group.grid(column=0, row=3)
variant.grid(column=0, row=4)

root.mainloop()