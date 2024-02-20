def generar_pares():
  """
  Genera una lista de números pares entre 1 y 100.

  Retorno:
    Una lista con los números pares entre 1 y 100.
  """

  return [numero for numero in range(1, 101) if numero % 2 == 0]

lista_pares = generar_pares()
print(f"Lista de números pares entre 1 y 100: {lista_pares}") 
