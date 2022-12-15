def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Число Фибоначчи:", fibonacci(int(input('Введите номер числа Фибоначчи, которое хотите вычислить: '))))