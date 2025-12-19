import pytest
from calculator.calculadora import raiz_cuadrada


def test_raiz_cuadrada_positiva():
    assert raiz_cuadrada(25) == 5


def test_raiz_cuadrada_cero():
    assert raiz_cuadrada(0) == 0


def test_raiz_cuadrada_negativa():
    with pytest.raises(ValueError):
        raiz_cuadrada(-9)
