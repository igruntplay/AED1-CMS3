from typing import Dict, Queue

# El tipo de fila debería ser Queue[int], pero la versión de Python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
    # Número de la última persona que llegó
    last_person:int = fila.qsize()
    # Tiempo de retorno para las personas que necesitan volver a la fila después de la Caja3
    return_times: Dict[int,int] = {}
    
    # Manejo de variables para manejar las cajas
    caja1_next: int = 1  # Próxima vez que la Caja1 estará libre
    caja2_next: int = 3  # Próxima vez que la Caja2 estará libre
    caja3_next: int = 2  # Próxima vez que la Caja3 estará libre

    for t in range(min + 1):  # Simulamos hasta el minuto dado
        # Cada 4 minutos llega una nueva persona
        if t % 4 == 0:
            last_person += 1
            fila.put(last_person) # Agrega a la nueva persona

        # Si alguien necesita volver a la fila en este minuto, los añadimos
        if t in return_times:
            fila.put(return_times[t]) # Añadimos a la fila a la persona que debía regresar a ella en el t minuto.
            del return_times[t] # Eliminamos entrada del diccionario (no se si lo necesito, pero vine renegando bastante, asi que por las dudas lo saco)
        # Verificamos qué cajas están disponibles y atendemos a las personas en orden
        if not fila.empty():
            if t == caja1_next:
                fila.get()
                caja1_next += 10  # La Caja1 estará libre de nuevo en 10 minutos
            elif t == caja2_next:
                fila.get()
                caja2_next += 4  # La Caja2 estará libre de nuevo en 4 minutos
            elif t == caja3_next:
                # La persona vuelve a la fila después de 3 minutos
                return_times[t + 3] = fila.get()
                caja3_next += 4  # La Caja3 estará libre de nuevo en 4 minutos

    return fila



if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)

