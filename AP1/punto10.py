import math

def factorial(numero):
  """
  Calcula el factorial de un número dado.

  Parámetros:
    numero: El número del que se quiere calcular el factorial (un número entero no negativo).

  Retorno:
    El factorial del número (un número entero).
  """

  if numero < 0:
    raise ValueError("El número no puede ser negativo.")

  return math.factorial(numero)


numero = int(input("Introduce un número: "))
try:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
except ValueError as error:
    print(error)