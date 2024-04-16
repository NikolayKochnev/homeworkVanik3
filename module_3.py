# Округление

print(round(4.5675, 3))


# Факториал

n = int(input())

factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)


# Фибоначи

fib1 = 1
fib2 = 1

n = int(input('Введите номер Фибоначи: '))

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print(fib2)