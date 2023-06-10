# En desarrollo
def test(program, expected: any, *args) -> bool:
    res: bool = program(*args) == expected
    print('Esperado: ', expected)
    print('Salida: ', program(*args))
    print(res)
