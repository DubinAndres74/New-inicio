from math import pi

class Circulo:
  """
  Clase que representa un círculo.
  """

  def __init__(self, centro, radio):
    """
    Inicializa un nuevo objeto Círculo.

    Args:
      centro (tuple): Tupla de dos coordenadas (x, y) que define el centro del círculo.
      radio (float): El radio del círculo.
    """
    self.centro = centro
    self.radio = radio

  def area(self):
    """
    Calcula el área del círculo.

    Returns:
      float: El área del círculo.
    """
    return pi * self.radio**2

  def perimetro(self):
    """
    Calcula el perímetro del círculo.

    Returns:
      float: El perímetro del círculo.
    """
    return 2 * pi * self.radio

  def pertenece(self, punto):
    """
    Indica si un punto pertenece al círculo.

    Args:
      punto (tuple): Tupla de dos coordenadas (x, y) que define el punto a verificar.

    Returns:
      bool: True si el punto pertenece al círculo, False en caso contrario.
    """
    distancia_al_centro = ((punto[0] - self.centro[0])**2 + (punto[1] - self.centro[1])**2)**0.5
    return distancia_al_centro <= self.radio

# Ejemplo de uso
circulo = Circulo((0, 0), 5)
print(f"Área: {circulo.area()}")  
print(f"Perímetro: {circulo.perimetro()}")  
print(f"¿Pertenece el punto (8, 1)?: {circulo.pertenece((3, 8))}")  
print(f"¿Pertenece el punto (3, 3)?: {circulo.pertenece((3, 3))}")  
