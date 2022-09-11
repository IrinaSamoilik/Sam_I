# урок 13, задание 1
class TheExample: # создание класса Exaple
    # создание статических переменных и они же являются глобальными  
    a = 2
    b = 3
    # создание динамических переменных
    def __init__(self, t, r):
        self.t = t
        self.r = r
    #первая функция
    def func(self):
        self.c = 5
        print(self.c)
    # вторая функция
    def func1(self):
        return self.a + self.b
    # третья функция
    def func2(self):
        return self.t**self.r
example = TheExample (4, 2)
print(example.a) #2
print(example.func1()) # 2+3 = 5
print(example.func2()) # t в степени r (4*4) = 16
example.func()