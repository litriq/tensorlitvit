def enc(s): 
    print(f'List of Words ={s.split()}')
    print(type(s.split()))
    b = s.encode('utf-8')
    print("Кодирование:",b)
enc('My name is Gustav')

def dec(s):
    print("Декодирование:",s.decode('utf-8'))
dec(b'My name is`nt Gustav')