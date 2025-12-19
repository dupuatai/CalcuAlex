from calculator.calculadora import sumar, potencia


def test_flujo_potencia():
    """
    Integra suma + potencia.
    (2 + 3) ^ 2 = 25
    """
    base = sumar(2, 3)  # 5
    resultado = potencia(base, 2)
    assert resultado == 25
