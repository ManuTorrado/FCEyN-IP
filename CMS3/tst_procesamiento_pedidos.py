from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dic[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"


def hayStockSuficiente(nombre, cantidad, stock) -> bool:
    res: bool = stock[nombre] >= cantidad
    return res


def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    res: List[Dict[str, Union[int, str, float, Dict[str, int]]]] = []
    while (not pedidos.empty()):

        curr_pedido = pedidos.get()
        curr_client = {
            'id': curr_pedido['id'], 'cliente': curr_pedido['cliente'], 'productos': {}, 'precio_total': 0.0, 'estado': 'completo'}
        productos = curr_pedido['productos']
        for producto in productos:

            if (hayStockSuficiente(producto, productos[producto], stock_productos)):

                curr_client['precio_total'] += precios_productos[producto] * \
                    productos[producto]
                curr_client['productos'][producto] = productos[producto]
                stock_productos[producto] -= productos[producto]
            else:

                curr_client['estado'] = 'incompleto'
                curr_client['productos'][producto] = stock_productos[producto]
                curr_client['precio_total'] += precios_productos[producto] * \
                    stock_productos[producto]
                stock_productos[producto] = 0
        res.append(curr_client)

    return res


# Ejemplo input
"""
pilaPedidos = Queue()


pedidost = [{"id": 21, "cliente": "Gabriela", "productos": {"Manzana": 2}}, {
    "id": 1, "cliente": "Juan", "productos": {"Manzana": 2, "Pan": 4, "Factura": 6}}]
stock_productost = {"Manzana": 10, "Leche": 5, "Pan": 3, "Factura": 0}
precios_productost = {"Manzana": 3.5, "Leche": 5.5, "Pan": 3.5, "Factura": 5}


for val in pedidost:
    pilaPedidos.put(val)

print(procesamiento_pedidos(pilaPedidos, stock_productost, precios_productost))
"""

npedidos = [{
    'id': 21,
    'cliente': 'Gabriela',
    'productos': {'Manzana': 2}
}, {
    'id': 1,
    'cliente': 'Juan',
    'productos': {'Manzana': 2, 'Pan': 4, 'Factura': 6}
}]

stockProductos = {'Manzana': 10, 'Leche': 5, 'Pan': 3, 'Factura': 0}
precioProductos = {'Manzana': 3.5, 'Leche': 5.5, 'Pan': 3.5, 'Factura': 2.75}

pilaPedidos = Queue()

for val in npedidos:
    pilaPedidos.put(val)

print(procesamiento_pedidos(pilaPedidos, stockProductos, precioProductos))
