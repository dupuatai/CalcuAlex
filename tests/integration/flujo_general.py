from calculator.calculadora import sumar, restar, multiplicar, dividir


def test_flujo_basico():
    """
    Flujo tonto pero integra varias operaciones:
    ((2 + 3) * 4 - 5) / 5 = 3
    """
    resultado = sumar(2, 3)               # 5
    resultado = multiplicar(resultado, 4) # 20
    resultado = restar(resultado, 5)      # 15
    resultado = dividir(resultado, 5)     # 3
    assert resultado == 3
