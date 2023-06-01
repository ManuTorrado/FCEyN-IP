from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista,
# la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.


def mesetaMasLarga(l: List[int]) -> int:

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


def hayMesetaDeLong(l: List[int], n: int) -> bool:
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


def todosIguales(l: List[int], i: int, j: int) -> bool:
    res: bool = True
    for x in range(i, j+1):
        if (not (l[x] == l[i])):
            res = False
            break

    return res


if __name__ == '__main__':
    x = input()
    print(mesetaMasLarga([int(j) for j in x.split()]))
