import math

# Ejercicio 1

# 1)


def raizDe2():
    return round(math.sqrt(2), 4)

# 2)


def imprimir_hola():
    print("hola")

# 3)


def imprimir_un_verso():
    print("Yeah Perdonen, Kamehameha")
    print("Después del tema del Tetris viene el Dragon Ball Rap")
# 4)


def factorial_de_2():
    return 2

# 5,6,7)
# Me pedia una banda de factoriales, hice el generico para ahorrar tiempo


def factorial_de(x: int):
    if (x == 0):
        return 1
    else:
        return x*factorial_de(x-1)

# Ejercicio 2

# 1


def imprimir_saludo(x: str):
    print("Hola " + x)

# 2


def raiz_cuadrada_de(x: int):
    return math.sqrt(x)

# No devuelvo directamente el valor de verdad porque en clase hablamos de la importancia de mantener el tipado


def es_multiplo_de(n: int, m: int) -> bool:
    res: bool = (n % m == 0)
    return res

# Ejercicio 3

# 3.1


def alguno_es_0(numero1, numero2) -> bool:
    res: bool = numero1 == 0 or numero2 == 0
    return res
# 3.2


def ambos_son_0(numero1, numero2) -> bool:
    res: bool = numero1 == 0 and numero2 == 0
    return res


def es_nombre_largo(nombre: str) -> bool:
    res: bool = (3 >= len(nombre) and len(nombre) <= 8)
    return res

# Ejercicio 4


def peso_pino(cms: int) -> int:
    res: int
    if (cms <= 3000):
        res = cms * 3
    else:
        res = cms * 2
    return res


def es_peso_util(peso: int) -> int:
    res: bool = peso >= 400 and peso <= 1000


def sirve_pino(altura: int) -> int:
    res: bool = es_peso_util(peso_pino(altura))
    return res


# Ejercicio 5, 1
def devolver_el_doble_si_es_par(x: int) -> int:
    res: int = x
    if (x % 2 == 0):
        res = x*2
    return res

# Ejercicio 7
# 1


def del_1_al_10():
    x: int = 0
    while (x < 10):
        print(x + 1)
        x += 1

# 2


def pares_entre_10_40():
    x: int = 10
    while (x <= 40):
        if (x % 2 == 0):
            print(x)
        x += 1

# 3


def decir_eco_diez_veces():
    x: int = 0
    while (x < 10):
        print('eco')
        x += 1
# 4


def cuenta_regresiva(x: int):
    while (x > 0):
        print(x)
        x -= 1
    print("Despegue")


# Ejercicio 7
def inr_del_1_al_10():
    for num in range(1, 11):
        print(num)
