class Rectangulo:
  """
  Clase que representa un rectángulo.
  """

  def __init__(self, punto_1, punto_2):
    """
    Inicializa un nuevo objeto Rectángulo.

    Args:
      punto_1 (tuple): Tupla de dos coordenadas (x, y) que define la primera esquina del rectángulo.
      punto_2 (tuple): Tupla de dos coordenadas (x, y) que define la segunda esquina del rectángulo.
    """
    self.punto_1 = punto_1
    self.punto_2 = punto_2

  def perimetro(self):
    """
    Calcula el perímetro del rectángulo.

    Returns:
      float: El perímetro del rectángulo.
    """
    lado_1 = abs(self.punto_1[0] - self.punto_2[0])
    lado_2 = abs(self.punto_1[1] - self.punto_2[1])
    return 2 * (lado_1 + lado_2)

  def area(self):
    """
    Calcula el área del rectángulo.

    Returns:
      float: El área del rectángulo.
    """
    lado_1 = abs(self.punto_1[0] - self.punto_2[0])
    lado_2 = abs(self.punto_1[1] - self.punto_2[1])
    return lado_1 * lado_2

  def es_cuadrado(self):
    """
    Indica si el rectángulo es un cuadrado.

    Returns:
      bool: True si el rectángulo es un cuadrado, False en caso contrario.
    """
    lado_1 = abs(self.punto_1[0] - self.punto_2[0])
    lado_2 = abs(self.punto_1[1] - self.punto_2[1])
    return lado_1 == lado_2

# Ejemplo de uso
rectangulo = Rectangulo((0, 0), (5, 10))
print(f"Perímetro: {rectangulo.perimetro()}")  
print(f"Área: {rectangulo.area()}")  
print(f"¿Es cuadrado?: {rectangulo.es_cuadrado()}")  

rectangulo_cuadrado = Rectangulo((0, 0), (5, 5))
print(f"¿Es cuadrado?: {rectangulo_cuadrado.es_cuadrado()}") 


