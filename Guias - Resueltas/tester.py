# En desarrollo

# Se introduce la funcion, el resultado que esperamos y los argumentos de la funcion
def test(program, expected: any, *args) -> bool:
    res: bool = program(*args) == expected
    print('Esperado: ', expected)
    print('Salida: ', program(*args))
    return res


# Sirve para hacer varios tests en una sola funcion
def multipleTest(program, cases: list[any], args: list[any]) -> bool:
    res: bool = True
    aux: int = 0
    for case in cases:
        if (test(program, case, args[aux]) == False):
            res = False
            print('Test fails')
        aux += 1
    return res
