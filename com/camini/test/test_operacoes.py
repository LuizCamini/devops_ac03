  
def funcao(var):
	return var + 5

def test1_positivo():
	assert funcao(10) == 15

def test2_negativo():
	assert funcao(-10) == -5

def test3_zero():
	assert funcao(0) == 5