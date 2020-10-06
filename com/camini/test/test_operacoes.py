def funcao(var):
    return var + 6

def test_1_positivo():
    assert func(12) == 18

def test_2_negativo():
    assert func(-12) == -6

def test_3_zero():
    assert func(0) == 6