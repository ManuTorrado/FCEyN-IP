
from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"


def atenderCaja3(fila: Queue, filaAlternativa):
    curr_cliente: int = fila.get()
    filaAlternativa.append({'id': curr_cliente, 'tiempo_espera': 3})


def atenderFila(fila: Queue):

    if (not fila.empty()):
        fila.get()


def eliminarEsperaFila3(fila):
    # Eliminar elementos con un criterio específico
    elementos_a_eliminar = []
    for diccionario in fila:
        if diccionario["tiempo_espera"] == 0:
            elementos_a_eliminar.append(diccionario)

    for elemento in elementos_a_eliminar:
        fila.remove(elemento)


def avanzarFila(fila: Queue, min: int):
    caja1AtendioHace: int = 0
    caja2AtendioHace: int = 0
    caja3AtendioHace: int = 0

    personasVolviendoFila3 = []

    # 10:00
    fila.put(fila.qsize() + 1)
    ultimoNumero = fila.qsize()

    # 10:01, atiendo caja 1
    if (min >= 1):
        atenderFila(fila)
    # 10:02, atiendo caja 3
    if (min >= 2 and not fila.empty()):
        curr_cliente: int = fila.get()
        personasVolviendoFila3.append({'id': curr_cliente, 'tiempo_espera': 1})

    # 10:03, atiendo caja 2
    if (min >= 3):
        atenderFila(fila)

    # Desde aca son las 10:03
    caja1AtendioHace = 2
    caja2AtendioHace = 0
    caja3AtendioHace = 1

    aux: int = 4

    hayGenteCon0 = False
    while (not fila.empty() and min+1 > aux):

        # Reviso si pasaron 4 minutos para agregar a la nueva persona

        if ((aux % 4) == 0):
            fila.put(ultimoNumero + 1)
            ultimoNumero += 1

        for persona in personasVolviendoFila3:

            if (persona['tiempo_espera'] == 0):
                fila.put(persona['id'])
                hayGenteCon0 = True

            else:
                persona['tiempo_espera'] -= 1

        if (hayGenteCon0):
            eliminarEsperaFila3(personasVolviendoFila3)
            hayGenteCon0 = False

        if (caja1AtendioHace == 10):
            atenderFila(fila)
            caja1AtendioHace = 0

        elif (caja2AtendioHace == 4):
            atenderFila(fila)
            caja2AtendioHace = 0

        elif (caja3AtendioHace == 4):
            atenderCaja3(fila, personasVolviendoFila3)
            caja3AtendioHace = 0

        aux += 1
        caja1AtendioHace += 1
        caja2AtendioHace += 1
        caja3AtendioHace += 1


Fila = Queue()
Fila.put(1)
Fila.put(2)
Fila.put(3)
Min = 5
avanzarFila(Fila, Min)

while (not Fila.empty()):
    print(Fila.get())
