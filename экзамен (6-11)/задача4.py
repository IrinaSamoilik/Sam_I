# задача 4
a = {5, 3, 7}
b = {4, 3, 8}
if a == b:
    print('Множества равны')
else:
    print('Множества не равны')
if a.issubset(b):
    print('Множество a состоит из множества b', a - b)
else:
    print('Множество b состоит из множества a', b - a)
if a&b:
    print('Элементы множеств пересекаются:', a & b)
else:
    print('Элементы множеств не пересекаются')