from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
# Definicion de la funcion de procesamiento de pedidos
def procesamiento_pedidos(pedidos: Queue, stock_productos: Dict[str, int], precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    res = []  # Resultado final, una lista de diccionarios que representan los pedidos procesados.

    while not pedidos.empty():
        pedido = pedidos.get()  # Tomar el primer pedido de la cola.

        precio_total = 0  # Inicializar el precio total del pedido a 0.
        estado = "completo"  # Asumir que el pedido se completará.

        for producto, cantidad in pedido['productos'].items():
            # Verificar si hay suficiente stock del producto.
            if stock_productos[producto] < cantidad:
                cantidad = stock_productos[producto]  # Si no hay suficiente stock, ajustar la cantidad a la disponible.
                estado = "incompleto"  # Marcar el pedido como "incompleto".

            # Actualizar el stock del producto.
            stock_productos[producto] -= cantidad

            # Calcular el precio del producto y agregarlo al precio total del pedido.
            precio_total += cantidad * precios_productos[producto]

            # Actualizar la cantidad del producto en el pedido a la cantidad realmente procesada.
            pedido['productos'][producto] = cantidad

        # Agregar el precio total y el estado al pedido.
        pedido.update({"precio_total": precio_total, "estado": estado})

        res.append(pedido)  # Agregar el pedido procesado a la lista de resultados.

    return res


if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input  
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}