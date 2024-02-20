

def area_circulo(radio):
  """
  Calcula el área de un círculo dado su radio.

  Parámetros:
    radio: El radio del círculo (un número real).

  Retorno:
    El área del círculo (un número real).
  """

  pi = 3.141592653589793
  area = pi * radio**2
  return area 

radio = float(input("Introduce el radio del círculo: "))
area = area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area}") 
