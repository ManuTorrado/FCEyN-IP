import math

def raizDe2():
    return round(math.sqrt(2),4)

def imprimir_hola():
    print("hola")

def imprimir_un_verso():
    print("Yeah Perdonen, Kamehameha")
    print("Después del tema del Tetris viene el Dragon Ball Rap")

def factorial_de_2():
    return 2

# Me pedia una banda de factoriales, hice el generico para ahorrar tiempo
def factorial_de(x:int):
    if(x == 0): 
        return 1
    else:
        return x*factorial_de(x-1)    


def imprimir_saludo(x:str):
    print("Hola " + x)

def raiz_cuadrada_de(x:int):
    return math.sqrt(x)   

# No devuelvo directamente el valor de verdad porque en clase hablamos de la importancia de mantener el tipado
def es_multiplo_de(n: int, m:int )-> bool:
    res: bool = (n%m == 0)
    return res

## Ejercicio 3

#3.1
def alguno_es_0(numero1, numero2)-> bool: 
    res:bool = numero1 == 0 or numero2 == 0
    return res
#3.2
def ambos_son_0(numero1, numero2)-> bool:
    res:bool = numero1 == 0 and numero2 == 0
    return res

def es_nombre_largo(nombre:str) -> bool:
    return 3 >= len(nombre) and len(nombre) <= 8


