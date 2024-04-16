def add(a, b):
    return a + b


print(add(2,3))


def subtract(a, b):
    return a - b


print(subtract(3,5))


def multiply(a, b):
    return a * b


print(multiply(4,5))


def divide(a, b):
    if b == 0:
        return 'Ошибка: деление на ноль'
    return a / b


print(divide(4,4))
