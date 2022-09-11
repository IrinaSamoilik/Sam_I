# Очень важная функция, может понадобиться на собеседовании (РЕКУРСИВНАЯ ФУНКЦИЯ)
def factorial (n):
    if n !=0:
        return n * factorial(n-1)
    else:
        return 1
print(factorial(5))