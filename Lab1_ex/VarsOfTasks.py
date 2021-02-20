import math

def task1(a, c):
    y1 = math.sqrt(a + c) + 1 / (a + c)
    return y1

def task2():
    a = 57.567
    b = -11.675
    c = -34.114
    d = b * b - 4 * a * c
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2

def task3(list_a, list_c, list_g, f):
    res = 0
    for i in range(10):
        solution = (list_a[i] ** 2 + 56 * list_c[i] * f * list_g[i])
        res += solution
    return res

