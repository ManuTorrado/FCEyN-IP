from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
  # Implementar esta funcion
  return 0

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))