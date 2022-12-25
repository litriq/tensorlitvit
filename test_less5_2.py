import less5_2


def test_func_str_str():
    assert less5_2.func('Я ','Ты') == 'Я Ты'

def test_func_int_int():
    assert less5_2.func(1, 2) == 3

def test_func_str_int():
    assert less5_2.func('akz', 2) == 'can only concatenate str (not "int") to str'

def test_func_int_str():
    assert less5_2.func(1, '1') == 'can only concatenate str (not "int") to str'

def test_func_str_int():
    assert less5_2.func('1', 2) == 'can only concatenate str (not "int") to str'