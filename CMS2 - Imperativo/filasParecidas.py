from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.


def filasParecidas(m: List[List[int]]) -> bool:
    res: bool = existeSolucion(m)
    return res


def existeSolucion(l: List[List[int]]) -> bool:
    res: bool = True
    i: int = 1
    n: int = l[1][0] - l[0][0]

    while (i < len(l)):
        for j in range(0, len(l[0])):
            if (not (l[i][j] - l[i-1][j] == n)):
                res = False
                break

        i += 1
    return res


if __name__ == '__main__':
    filas = int(input())
    columnas = int(input())

    matriz = []

    for i in range(filas):
        fila = input()
        if len(fila.split()) != columnas:
            print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
        matriz.append([int(j) for j in fila.split()])

    print(filasParecidas(matriz))
