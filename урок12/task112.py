# урок 12 задание 3
import math
def square (a):
    P = 4 * a
    S = a ** 2
    d = math.sqrt (2) * a
    return P, S, d

print(square(int(input('введите сторону квадрата:'))))
