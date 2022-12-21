import math
import cmath


print('\nНу привет, давай помогу решить тебе квадратное уравнение :-)\n')
print('Формула квадратного  уравнения: ax^2 + bx + c = 0')
print('Мне нужны значения a, b и с')
a = complex(input('a = '))
b = complex(input('b = '))
c = complex(input('c = '))

discr = b**2 - 4*a*c
print('Дискриминант D = %s' % discr)
if a == 0 and b == 0 and c == 0:
    print('Корнем является любое число')
else:    
    if a == 0 and b == 0:
        print ('решений нет')
    else:
        if a == 0 and c == 0:
            print('x=', 0)
        else:
            if a == 0:
                x = (-c / b)
                print('x=', x)
            else:
                if b == 0:
                    print('x=', math.sqrt(-c / a))
                else:
                    d = b*b - 4*a*c
                    x1 = (-b + cmath.sqrt(d))/(2*a)
                    x2 = (-b - cmath.sqrt(d))/(2*a)
                    print('x1=',x1)
                    print('x2=',x2)
