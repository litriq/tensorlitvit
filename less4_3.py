import random
    #Множество а
a = set()
for i in range(10):
    a.add(random.randint(1,15))
print('Первое множество:', a)
    #Множество b
b = set()
for i in range(10):
    b.add(random.randint(1,15))
print('Второе множество:', b)
    #Выводы
print('Есть и там и там:',a.intersection(b))
print('Только в а:', a.difference(b))
print('Только в b:', b.difference(a))
print('Значения в а или в б, но которых нет одновременно в а и б:', b.difference(a), a.difference(b))