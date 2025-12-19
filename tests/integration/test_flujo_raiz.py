from calculator.calculadora import sumar, raiz_cuadrada


def test_flujo_raiz():
    """
    Integra suma + raíz cuadrada.
    sqrt(9 + 7) = sqrt(16) = 4
    """
    valor = sumar(9, 7)
    resultado = raiz_cuadrada(valor)
    assert resultado == 4
