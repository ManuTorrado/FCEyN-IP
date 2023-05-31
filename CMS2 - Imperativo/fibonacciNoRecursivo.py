import sys


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


if __name__ == '__main__':
    x = int(input())
    print(fibonacciNoRecursivo(x))
