from queue import LifoQueue


# para el tipo pila de enteros, usar: "pila: LifoQueue". La notación "pila: LifoQueue[int]" no funciona.
# Operadores validos: * + / -


# La utilizo junto con 'esOperador' para checkear si un elemento de la pila es un signo
def pertenece(c: list, z: any) -> bool:
    res: bool = False
    for j in c:
        if (j == z):
            res = True
            break
    return res


def esOperador(m: str) -> bool:
    res: bool = pertenece(['+', '-', '*', '/'], m)
    return res


def operacionBinaria(operando1: float, operando2: float, operador: str) -> float:
    if (operador == '+'):
        res = operando2 + operando1
    elif (operador == '-'):
        res = operando2 - operando1
    elif (operador == '*'):
        res = operando2 * operando1
    elif (operador == '/'):
        res = operando2 / operando1

    return res


def operar(pila: LifoQueue) -> float:
    res: float = 0.0
    operador = pila.get()
    termino1 = pila.get()
    termino2 = pila.get()

    # los siguientes terminos son 2 operaciones
    if (esOperador(termino1) and esOperador(termino2)):
        res += operacionBinaria(operar(pila), operar(pila), operador)

    # termino 1 es operacion, termino 2 es numero
    elif (esOperador(termino1)):
        pila.put(termino1)
        res += operacionBinaria(operar(pila), float(termino2), operador)

    # termino 2 es operacion, termino 1 es numero
    elif (esOperador(termino2)):
        pila.put(termino2)
        res += operacionBinaria(operar(pila), float(termino1), operador)

    # Ambos terminos son 2 numeros, puedo operar
    else:
        res += operacionBinaria(float(termino1), float(termino2), operador)

    return res


def calcular_expresion(expr: str) -> float:
    res: float = 0.0
    aplanado: list[str] = expr.split()
    pila: LifoQueue = LifoQueue()
    # Llenar la pila
    for elem in aplanado:
        pila.put(elem)

    res = operar(pila)

    return res


# Casos de test
print(calcular_expresion('5 2 +'))  # 7
print(calcular_expresion('5 2 - 4 *'))  # 17
print(calcular_expresion('2 5 * 7 +'))  # 17.0
print(calcular_expresion('2 3.5 -'))  # -1.5
print(calcular_expresion('2 -3.5 +'))  # -1.5
