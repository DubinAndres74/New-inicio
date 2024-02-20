def sumar_lista(lista):
  """
  Calcula la suma de los números en una lista.

  Parámetros:
    lista: La lista de números (una lista de números enteros).

  Retorno:
    La suma de los números en la lista (un número entero).
  """

  for numero in lista:
    if not isinstance(numero, int):
      raise ValueError("La lista debe contener solo números enteros.")

  return sum(lista)

# Ejemplo de uso
lista_numeros = [8, 9, 5, 3, 5]
try:
    suma = sumar_lista(lista_numeros)
    print(f"La suma de la lista {lista_numeros} es: {suma}")
except ValueError as error:
    print(error)