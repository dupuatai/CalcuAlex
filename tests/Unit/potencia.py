from calculadora import potencia


def test_potencia_basica():
    assert potencia(2, 3) == 8


def test_potencia_exponente_cero():
    assert potencia(5, 0) == 1


def test_potencia_exponente_uno():
    assert potencia(7, 1) == 7
