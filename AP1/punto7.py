def encontrar_max_min(lista):
  """
  Encuentra el número más grande y el más pequeño en una lista.

  Parámetros:
    lista: La lista de números (una lista de números enteros).

  Retorno:
    Una tupla con el número más grande y el número más pequeño en la lista.
  """

  if not lista:
    raise ValueError("La lista no puede estar vacía.")

  return max(lista), min(lista)

# Ejemplo de uso
lista_numeros = [15, 2, 299, 24, 96, 9, -1]
try:
    maximo, minimo = encontrar_max_min(lista_numeros)
    print(f"El número más grande en la lista {lista_numeros} es: {maximo}")
    print(f"El número más pequeño en la lista {lista_numeros} es: {minimo}")
except ValueError as error:
    print(error)