def func(z = 0, *args):
    """Сложение строк или чисел
        
    Принимает:
        z - для записи суммы переменных
        *args - переменные, которые будут складываться

    Возвращает:
        z - сумму переменных
    """
    try:
        if type(args) == str:
            z = ''
        if type(args) == int or type(args) == float:
            z = 0
        for num in args:
            z += num
        return z
    except TypeError as e:
        z = e
    return z

print(func(10,1))
print(func(10))
print(func(10,0,0,1,1))
print(func('Ssq', 'qwa'))
print(func(1.0011, 314.2))
print(func())
print(func('12a', 1))
