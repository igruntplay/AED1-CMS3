from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"

# El tipo de fila debería ser Queue[int], pero la versión de Python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int) -> list:
    n: int = fila.qsize()  # Número de personas en la fila
    caja1: int = 1  # Momento en el que caja1 atiende
    caja2: int = 3  # Momento en el que caja2 atiende
    caja3: int = 2  # Momento en el que caja3 atiende
    caja3_regresa: int = -1  # Momento en que la persona atendida por caja3 regresa a la fila
    persona: int = -1  # Persona atendida por caja3
    tiempo: int = 0  # Variable que controla el tiempo transcurrido
    fila_final = []  # Fila final después de avanzar los minutos dados

    while tiempo <= min:  # Simulamos el paso del tiempo
        # Cada 4 minutos a partir de las 10:00, llega una nueva persona a la fila
        if tiempo != 0 and tiempo % 4 == 0:
            n += 1
            fila.put(n)

        # Verificamos si es el tiempo en que la persona atendida por Caja3 debe regresar a la fila
        if tiempo == caja3_regresa and persona != -1:
            fila.put(persona)
            persona = -1
            caja3_regresa = -1

        # Verificamos si es el tiempo para que Caja1 atienda a la siguiente persona
        if tiempo == caja1 and not fila.empty():
            fila.get()
            caja1 += 10  # Caja1 puede atender a la siguiente persona en 10 minutos

        # Verificamos si es el tiempo para que Caja2 atienda a la siguiente persona
        if tiempo == caja2 and not fila.empty():
            fila.get()
            caja2 += 4  # Caja2 puede atender a la siguiente persona en 4 minutos

        # Verificamos si es el tiempo para que Caja3 atienda a la siguiente persona
        if tiempo == caja3 and not fila.empty() and persona == -1:
            persona = fila.get()
            caja3 += 4  # Caja3 puede atender a la siguiente persona en 4 minutos
            caja3_regresa = tiempo + 3  # La persona atendida por Caja3 regresa a la fila en 3 minutos

        tiempo += 1  # Avanzamos el tiempo

    while not fila.empty():  # Al final, trasladamos los restantes de la fila a la fila_final
        fila_final.append(fila.get())

    return fila_final

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

