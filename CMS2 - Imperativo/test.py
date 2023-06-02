from typing import List
from typing import Tuple
# Ejercicio 1


def quienGana(j1: str, j2: str) -> str:
    res: str = ''
    if (gana(j1, j2)):
        res = "Jugador1"
    if (gana(j2, j1)):
        res = "Jugador2"
    if ((not gana(j1, j2)) and (not gana(j2, j1))):
        res = "Empate"
    return res


def juegaBien(j: str) -> bool:
    res: bool = (j == "Piedra" or j == "Papel" or j == "Tijera")
    return res


def gana(j1: str, j2: str) -> bool:
    res: bool = piedraGanaATijera(j1, j2) or tijeraGanaAPapel(
        j1, j2) or papelGanaAPiedra(j1, j2)
    return res


def piedraGanaATijera(j1: str, j2: str) -> bool:
    res: bool = (j1 == "Piedra" and j2 == "Tijera")
    return res


def tijeraGanaAPapel(j1: str, j2: str) -> bool:
    res: bool = (j1 == "Tijera" and j2 == "Papel")
    return res


def papelGanaAPiedra(j1: str, j2: str) -> bool:
    res: bool = (j1 == "Papel" and j2 == "Piedra")
    return res


# Casos de test ej 1
def testQuienGana():
    jugadas: list[str] = ['Piedra', 'Papel', 'Tijera']
    count: int = 0
    # Casos jugador 1
    while (count < len(jugadas)):
        for play in jugadas:
            print('Jugador 1: ' + play + ', Jugador 2: ' + jugadas[count])
            print('Resultado: ' + quienGana(play, jugadas[count]))
        count += 1
    # Casos jugador 2
    count = 0
    print(" ----------------------------- ")
    while (count < len(jugadas)):
        for play in jugadas:
            print('Jugador 1: ' + jugadas[count] + ', Jugador 2: ' + play)
            print('Resultado: ' + quienGana(jugadas[count], play))
        count += 1


# testQuienGana()
# Ejercicio 2


def todosIguales(l: list[int], i: int, j: int) -> bool:
    res: bool = True
    for x in range(i, j+1):
        if (not (l[x] == l[i])):
            res = False
            break

    return res


def fibonacciNoRecursivo(n: int) -> int:
    res: int = 0

    if (n == 0):
        return 0
    if (n == 1):
        return 1
    seq: list[int] = [1, 1]
    count: int = 2
    while (count < n):
        seq.append(seq[count-1] + seq[count-2])
        count += 1
    res = seq[len(seq)-1]

    return res


# print(todosIguales([1, 4, 1, 1], 0, 3))


# Casos de testing para Ej2 CMS2
"""
print("fibonacci 0: " + str(fibonacciNoRecursivo(0)))
print("fibonacci 1: " + str(fibonacciNoRecursivo(1)))
print("fibonacci 2: " + str(fibonacciNoRecursivo(2)))
print("fibonacci 3: " + str(fibonacciNoRecursivo(3)))
print("fibonacci 4: " + str(fibonacciNoRecursivo(4)))
print("fibonacci 5: " + str(fibonacciNoRecursivo(5)))
print("fibonacci 6: " + str(fibonacciNoRecursivo(6)))
print("fibonacci 7: " + str(fibonacciNoRecursivo(7)))
print("fibonacci 8: " + str(fibonacciNoRecursivo(8)))
print("fibonacci 9: " + str(fibonacciNoRecursivo(9)))
print("fibonacci 10: " + str(fibonacciNoRecursivo(10)))

"""


def mesetaMasLarga(l: list[int]) -> int:

    res: int = 0
    count: int = 0
    if (len(l) == 0):
        return 0
    while (True):
        if (hayMesetaDeLong(l, count) and not hayMesetaDeLong(l, count + 1)):
            res = count
            break
        count += 1
    return res

# Ejercicio 3


def hayMesetaDeLong(l: list[int], n: int) -> bool:
    res: bool = False
    count: int = 0
    x: int = 0

    while (count < len(l)):
        if (x <= count):
            if (n == count-x+1 and todosIguales(l, x, count)):
                res = True
                break
            x += 1
        else:
            count += 1
            x = 0

    return res


def todosIguales(l: list[int], i: int, j: int) -> bool:
    res: bool = True
    for x in range(i, j+1):
        if (not (l[x] == l[i])):
            res = False
            break

    return res

# Casos de test ej 3


"""
print(mesetaMasLarga([1, 1, 2, 3]))  # Esperado: 2
print(mesetaMasLarga([2, 3, 1, 1]))  # Esperado: 2
print(mesetaMasLarga([1, 1, 2, 2, 2, 3, 3]))  # Esperado: 3
print(mesetaMasLarga([1, -2, -2, -2, 3, 3, 4, 4, 5])),  # Esperado : 3
"""

# Ejercicio 4


def esMatriz(m: List[List[int]]) -> bool:
    if ((not (len(m) > 0)) or (not (len(m[0]) > 0))):
        return False

    res: bool = True
    for j in range(0, len(m)):
        if (not (len(m[j]) == len(m[0]))):
            res = False
            break
    return res


"""
def filasParecidasAanterior(m: List[int], n: int) -> bool:
    res: bool = True
    for i in range(1, len(m)):
        if (not filaAnteriorMasN(m, i, n)):
            res = False
            break
    return res
"""


def filaAnteriorMasN(m: List[int], i: int) -> bool:
    res: bool = True

    """
    for j in range(0, len(m[0])):
        if (not m[i][j] == m[i-1][j] + n):
            res = False
            break
            """

    return res


def filasParecidas(m: list[list[int]]) -> bool:
    print(m)
    res: bool = existeSolucion(m)
    return res


def existeSolucion(l: list[list[int]]) -> bool:
    res: bool = True
    i: int = 1
    n: int = l[1][0] - l[0][0]
    print("n = ", n)
    while (i < len(l)):

        for j in range(0, len(l[0])):
            print(l[i][j], " - ", l[i-1][j], ' =', l[i][j] - l[i-1][j])

            if (not (l[i][j] - l[i-1][j] == n)):
                res = False
                break

        i += 1
    return res

# Casos de test ej 4


def testear4():
    print(filasParecidas([[3], [3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))  # True
    print(filasParecidas([[3], [3], [-1, -2, -3],
                          [-1, -2, -3], [-1, -2, -3]]))  # True
    print(filasParecidas([[2], [3], [1, 2, 3], [-9, -10, -7]]))  # false
    print(filasParecidas([[5], [2], [100, 200], [
        5, 6], [1, 2], [1, 2], [1, 2]]))  # false

    # print(filasParecidas([[3], [3], [1, 2, 3], [-1, 0, 1], [-3, -2, -1]]))  # True

    print(filasParecidas([[3], [3], [-1, -2, -3],
                          [-2, -3, -4], [-3, -4, -5,]]))  # True


# Ejercicio 5


def hayVuelosDesde(origen: str, vuelos: List[Tuple[str, str]]) -> bool:
    res: bool = False

    for vuelo in vuelos:
        if (vuelo[0] == origen):
            res = True
            break

    return res


def hayVuelosHasta(destino: str, vuelos: List[Tuple[str, str]]) -> bool:
    res: bool = False

    for vuelo in vuelos:
        if (vuelo[1] == destino):
            res = True
            break

    return res


def hayRuta(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> bool:
    res: bool = True
    if (not hayVuelosHasta(destino, vuelos) or not hayVuelosDesde(origen, vuelos)):
        res = False

    return res


def vuelosDesde(origen: str,  vuelos: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    res: List[Tuple[str, str]] = []
    for vuelo in vuelos:
        if (vuelo[0] == origen):
            res.append(vuelo)

    return res


def buscarRuta(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    res: List[Tuple[str, str]] = []
    # esto asumiendo que los vuelos hacia el destino y desde el origen existen
    for vuelo in vuelosDesde(origen, vuelos):
        if vuelo[1] == destino:
            res.append(vuelo)
            break
        else:
            res.append(vuelo)
            res.extend(buscarRuta(vuelo[1], destino,
                                  vuelos))

    return res


def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int:
   # Implementar esta funcion
    if (not hayRuta(origen, destino, vuelos)):
        return -1
    res: int = len(buscarRuta(origen, destino, vuelos))

    return res

# Casos de test ejercicio 5


print(sePuedeLlegar('A', 'B', [('A', 'C'), ('C', 'B')]))  # 2
# print("------------------")
print(sePuedeLlegar('A', 'B', [('A', 'C'), ('C', 'D'), ('C', 'B')]))  # 3
# print("------------------")
print(sePuedeLlegar('A', 'B', [('A', 'C'), ('C', 'A')]))  # -1


print(sePuedeLlegar('rosario', 'buenos-aires', [('rosario', 'jujuy'),
      ('san-telmo', 'jujuy'), ('chubut', 'buenos-aires'), ('jujuy', 'chubut')]))  # 3

# def hayRuta(vuelos: list[Tuple[str, str]], origen: str, destino: str) -> bool:
# res: bool = len(buscarRuta(origen, destino, vuelos)) > 0

# vuelosValidos(ruta, vuelos)
# len(ruta) >= 1
# ruta[0] == origen
# ruta[len(ruta) - 1] == destino
# caminoDeVuelos(ruta)
#    return res
