import math


def alg1(a, b, c):
    y1 = (5 + c * math.sqrt(b + 5 * math.sqrt(a))) ** (1 / 3)
    return y1
# print(alg1(1, 2, 5))

def alg2(k, d):
    if k > 10:
        y = math.sqrt(k * math.sqrt(d ** 2) + d * math.sqrt(k ** 2))
    else:
        y = (k + d) ** 2
    return y

# print(alg2(12, 5))

def alg3(a, b):
    res_1 = 1
    res_2 = 0
    for i in range(len(a)-1):
        res_1 *= a[i] + b[i+1]
        res_2 += a[i+1] * b[i]
    f = res_1 + res_2
    return f

a_l = [1, 2, 5, 1, 4]
b_l = [1, 2, 5, 1, 4]
print(alg3(a_l, b_l))

