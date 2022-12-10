l = list(map(int, input('Заполните список (значения через пробел):\n').split()))
print('Вы ввели список: ', l)
len_l = len(l)
for i in range(len_l):
    for j in range(len_l-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print('Список, отсортированный пузырьком: ', l) 