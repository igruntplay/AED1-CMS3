from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,int]]) -> Dict[str,List[str]]:
  # Implementar esta funcion
  resultado = {}

      # Recorrer cada diccionario en la lista
  for diccionario in a_unir:
        # Para cada clave en el diccionario
        for clave, valor in diccionario.items():
            # Si la clave ya está en el resultado, añade el valor a la lista existente
            if clave in resultado:
                resultado[clave].append(valor)
            # Si la clave no está en el resultado, crea una nueva lista con el valor
            else:
                resultado[clave] = [valor]



  return resultado


if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))