import sys


def fibonacciNoRecursivo(n: int) -> int:
    # Implementar esta funcion
    return 0


def esSecuenciaFibonacci(l: list) -> bool:
    res: bool = ((len(l) > 0 and l[0] == 0) and (len(l) > 1 and l[1] == 1))

    return res


if __name__ == '__main__':
    x = int(input())
    print(fibonacciNoRecursivo(x))
