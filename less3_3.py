import math

print("\nНу привет, давай помогу решить тебе квадратное уравнение :-)\n")
print("Формула квадратного  уравнения: ax^2 + bx + c = 0")
print("Мне нужны значения a, b и с")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %s" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")
elif discr == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    print("Корней нет")