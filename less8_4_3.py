import time

def decor(func):
    def wrapper():
        time.sleep(1)
        print('Столица Нигерии? Сложновато, но я обязательно вычислю и дам ответ...')
        time.sleep(7)
        func()
    return wrapper

@decor
def add(*args):
    print('Абуджа')

add()
