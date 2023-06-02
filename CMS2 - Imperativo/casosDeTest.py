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

# Casos de testing para Ej2


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


# Casos de test ej 3


print(mesetaMasLarga([1, 1, 2, 3]))  # Esperado: 2
print(mesetaMasLarga([2, 3, 1, 1]))  # Esperado: 2
print(mesetaMasLarga([1, 1, 2, 2, 2, 3, 3]))  # Esperado: 3
print(mesetaMasLarga([1, -2, -2, -2, 3, 3, 4, 4, 5])),  # Esperado : 3


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


# Casos de test ejercicio 5

def testear5():
    print(sePuedeLlegar('A', 'B', [('A', 'C'), ('C', 'B')]))  # 2

    print(sePuedeLlegar('A', 'B', [('A', 'C'), ('C', 'D'), ('C', 'B')]))  # 3

    print(sePuedeLlegar('A', 'B', [('A', 'C'), ('C', 'A')]))  # -1

    print(sePuedeLlegar('rosario', 'buenos-aires', [('rosario', 'jujuy'),
                                                    ('san-telmo', 'jujuy'), ('chubut', 'buenos-aires'), ('jujuy', 'chubut')]))  # 3
