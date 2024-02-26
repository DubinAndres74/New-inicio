def calcular_operaciones(numero1, numero2):
  """
  Calcula la suma, resta, multiplicación y división de dos números.

  Parámetros:
    numero1: El primer número (un número entero).
    numero2: El segundo número (un número entero).

  Retorno:
    Un diccionario con los resultados de las operaciones.
  """

  operaciones = {
    "suma": numero1 + numero2,
    "resta": numero1 - numero2,
    "multiplicación": numero1 * numero2,
    "división": numero1 / numero2,
  }

  return operaciones


numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

operaciones = calcular_operaciones(numero1, numero2)

for operacion, resultado in operaciones.items():
  print(f"{operacion}: {resultado}")