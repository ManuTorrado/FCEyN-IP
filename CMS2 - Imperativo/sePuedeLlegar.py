from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.


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


if __name__ == '__main__':
    origen = input()
    destino = input()
    vuelos = input()

    print(sePuedeLlegar(origen, destino, [
          tuple(vuelo.split(',')) for vuelo in vuelos.split()]))
