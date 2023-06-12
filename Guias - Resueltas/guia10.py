from queue import LifoQueue as Pila
from queue import Queue as Cola
import random


# Ejercicio 1


# una forma de hacerlo
def contarlineas(nombre_archivo: str) -> int:
    f = open(nombre_archivo, "r")
    res: int = 0
    for l in f:
        res += 1
    return res

# otra forma


def contarlineas2(nombre_archivo: str) -> int:
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


# Ejercicio 2, incompleto
def clonarSinComentarios(nombre_archivo: str):
    f = open(nombre_archivo, "r")
    lines = f.readlines()
    f2 = open(nombre_archivo+" copia", "w")

    for line in lines:
        print(line.strip())
        if (line.strip()[0] == "#"):

            f2.write(line.strip()[1:] + '\n')
            continue
        f2.write(line)

    f2.close()


# clonarSinComentarios("hola.txt")

# Ejercicio 3


def reverso(nombre_archivo: str):
    f = open(nombre_archivo, 'r')
    f2 = open(nombre_archivo + ' reverso', 'w')
    lines: list[str] = f.readlines()
    count = len(lines)
    while (count > 0):
        f2.write(lines[count-1])
        count -= 1

    f2.close()


# reverso('hola.txt')

# Ejercicio 4


def agregarFraseAlFinal(nombre_archivo: str, frase: str):
    f = open(nombre_archivo, 'a')
    f.write('\n' + frase)
    f.close()

# agregarFrase('hola.txt', 'ultima')

# Ejercicio 5 (se puede mejorar?)


def agregarFraseAlPrincipio(nombre_archivo: str, frase: str):
    file_read = open(nombre_archivo, 'r')
    lines = file_read.read()
    file_read.close()
    f = open(nombre_archivo, 'w')
    f.write(frase + '\n' + lines)
    f.close()


# agregarFraseAlPrincipio('hola.txt', 'principio')

# Ejercicio 6 - revisar

def leerBinario(nombre_archivo: str):
    f = open(nombre_archivo, 'r')


# Ejercicio 7 - revisar

def promedioEstudiante(lu: str) -> float:
    res: float = 0
    csv: str = open("alumnos.csv", 'r')

    return res


def separadoPorComas(nombre_archivo: str):
    f = open(nombre_archivo, 'r')


# Pilas

# Ejercicio 8
def generarNrosAlAzar(n: int, desde: int, hasta: int) -> list[int]:
    res: list[int] = random.sample(range(desde, hasta), n)
    return res


# print(generarNrosAlAzar(5, 1, 10))

# Ejercicio 9


def armarPila(n: int, desde: int, hasta: int):
    res: Pila = Pila()
    for numero in generarNrosAlAzar(n, desde, hasta):
        res.put(numero)
    return res


# print(armarPila(5, 1, 10))

# Ejercicio 10


def cantidadElementosPila(p: Pila) -> int:
    res: int = 0
    while not p.empty():
        res += 1
        p.get()
    return res


def cantidadElementosPila2(p: Pila) -> int:
    res: int = p.qsize()
    return res


"""
p = Pila()
p.put(7)
p.put(3)
print(cantidadElementosPila(p))
"""


# Ejercicio 11


def buscarElMaximo(p: Pila) -> int:
    res: int = 0
    ind: int = 0
    while (ind < p.qsize()):
        if (p.get(ind) > res):
            res = p.get(ind)
    return res


""" 
p = Pila()
p.put(4)
p.put(7)
p.put(3)
print(buscarElMaximo(p))
"""

# Ejercicio 12
# Lo dejo para despues


def estaBienBalanceada(s: str) -> bool:
    res: bool = False

    return res


# 3. Colas

# Ejercicio 13

def generarNrosAlAzar(n: int, desde: int, hasta: int):
    lista: list[any] = generarNrosAlAzar(n, desde, hasta)
    c = Cola()
    for x in lista:
        c.put(x)
    return c

# Ejercicio 14


def cantidadElementosCola(c: Cola) -> int:
    res: int = 0
    while not c.empty():
        c.get()
        res += 1
    return res

# Forma alternativa


def cantidadElementosCola2(c: Cola) -> int:
    res = c.qsize()
    return res


"""
c = Cola()
c.put(1)
c.put(3)
print(cantidadElementosCola(c))
"""


# 4 Diccionarios

# Ejercicio 18
def agregarPorLongitud(nombre_archivo: str) -> dict:
    res: dict = {}
    f = open(nombre_archivo, 'r')
    lines: list[str] = f.readlines()
    for line in lines:
        aux: int = 0
        if ((len(line.split())) in res):
            res[(len(line.split()))] += 1
        else:
            res[(len(line.split()))] = 1
    print(res)
    return res


agregarPorLongitud('hola.txt')
# Ejercicio 19


def promedioAlumnos(nombre_archivo: str) -> int:
    res: int = 0
    return res

# Ejercicio 20


def laPalabraMasFrecuente(nombre_archivo: str) -> str:
    f = open(nombre_archivo, 'r')
