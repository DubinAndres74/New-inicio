import random

# Definir la cantidad de números aleatorios
cantidad_numeros = 10

# Generar una lista vacía para almacenar los números aleatorios
numeros_aleatorios = []

# Generar números aleatorios y agregarlos a la lista
for i in range(cantidad_numeros):
    numero_aleatorio = random.randint(1, 100)
    numeros_aleatorios.append(numero_aleatorio)

# Imprimir la lista de números aleatorios
print(numeros_aleatorios)