# Ejercicio de ayuda

def fibonacci(n: int) -> int:
    res: int = 1
    if (n > 2):
        res = fibonacci(n-1) + fibonacci(n-2)

    return res


def esSecuenciaFibonacci(l: list) -> bool:
    res: bool = False
    if (len(l) > 0):
        return l[0] == 0
    if ((len(l) > 1)):
        return l[1] == 1

    for j in l:
        if (2 <= j < len(l)):
            res = (l[j] == l[j-1] + l[j-2])
    return res


def fibonacciNoRecursivo(n: int) -> int:
    res: int = 0

    if (n == 0):
        return 1
    if (n == 1):
        return 1
    seq: list = [1, 1]
    count: int = 2
    while (count < n):
        seq.append(seq[count-1] + seq[count-2])
        count += 1
    res = seq[len(seq)-1]

    return res


print(fibonacciNoRecursivo(4))
