import math



def sumar(a: float, b: float) -> float:
    """Retorna la suma de a y b."""
    return a + b


def restar(a: float, b: float) -> float:
    """Retorna la resta de a y b."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna el producto de a y b."""
    return a * b


def decorador(func):
    """Valida que b no sea 0 antes de dividir."""
    def inner(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("No es posible dividir por 0")
        return func(a, b)
    return inner


@decorador
def dividir(a: float, b: float) -> float:
    """Retorna la división a / b."""
    return a / b

def potencia(a: float, b: float) -> float:
    """Retorna a elevado a la potencia b."""
    return a ** b

def calculadora():
    print("=== CALCULADORA ===")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) Potencia")

    opcion = input("Elige la operación (1-5): ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", sumar(num1, num2))
    elif opcion == "2":
        print("Resultado:", restar(num1, num2))
    elif opcion == "3":
        print("Resultado:", multiplicar(num1, num2))
    elif opcion == "4":
        print("Resultado:", dividir(num1, num2))
    elif opcion == "5":
        print("Resultado:", potencia(num1, num2))
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    calculadora()
