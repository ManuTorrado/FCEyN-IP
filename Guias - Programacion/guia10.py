# Ejercicio 1


# una forma de hacerlo
def contarlineas(nombre_archivo: str) -> int:
    f = open(nombre_archivo, "r")
    res: int = 0
    for l in f:
        res += 1
    return res

# otra forma


def contarlienas2(nombre_archivo: str) -> int:
    f = open(nombre_archivo, "r")
    res: int = len(f.readlines())
    return res


# Ejercicio 1 pto 2

def contiene(l: list, k: any) -> bool:
    res = False
    for j in l:
        if (j == k):
            res = True
            break
    return res


def existePalabra(palabra: str, archivo: str) -> bool:
    res: bool = False
    f = open(archivo, "r")
    lines = f.readlines()
    for line in lines:
        if (contiene(line.split(), palabra)):
            res = True
            break
    return res


# Ejercicio 1 pto 3
def apariciones(l: list, a: any) -> int:
    res: int = 0
    for j in l:
        if (j == a):
            res += 1
    return res


def cantidadApariciones(nombre_archivo: str, palabra: str) -> int:
    res: int = 0
    f = open(nombre_archivo, "r")
    lines: list = f.readlines()
    for line in lines:
        res += apariciones(line.split(), palabra)

    return res


print(cantidadApariciones("hola.txt", "com"))
