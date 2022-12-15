def func(z = 0, *args):
    if type(args) == str:
        z = ''
    if type(args) == int or type(args) == float:
        z = 0
    for num in args:
        z += num
    print(z)

func(10,1)
func(10)
func(10,0,0,1,1)
func('Ssq', 'qwa')
func(1.0011, 314.2)
func()