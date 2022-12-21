def func(z = 0, *args):
    """Сложение строк или чисел
        
    Принимает:
        z - для записи суммы переменных
        *args - переменные, которые будут складываться

    Возвращает:
        z - сумму переменных
    """
    if type(args) == str:
        z = ''
    if type(args) == int or type(args) == float:
        z = 0
    for num in args:
        z += num
    return z

func(10,1)
func(10)
func(10,0,0,1,1)
func('Ssq', 'qwa')
func(1.0011, 314.2)
func()
