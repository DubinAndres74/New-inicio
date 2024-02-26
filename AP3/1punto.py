class Vehiculo:
  """
  Clase que representa un vehículo genérico.
  """

  def __init__(self, velocidad_maxima, kilometraje):
    """
    Inicializa un nuevo objeto Vehículo.

    Args:
      velocidad_maxima (float): La velocidad máxima del vehículo en km/h.
      kilometraje (float): El kilometraje actual del vehículo en km.
    """
    self.velocidad_maxima = velocidad_maxima
    self.kilometraje = kilometraje

  def __str__(self):
    """
    Devuelve una representación textual del vehículo.

    Returns:
      str: Una cadena que describe el vehículo.
    """
    return f"Vehículo con velocidad máxima de {self.velocidad_maxima} km/h y un kilometraje de {self.kilometraje} km." 

vehiculo = Vehiculo(120, 10000)
print(vehiculo)  # Salida: "Vehículo con velocidad máxima de 120 km/h y un kilometraje de 10000 km."

vehiculo.kilometraje += 500  # Aumenta el kilometraje en 500 km.
print(vehiculo)  # Salida: "Vehículo con velocidad máxima de 120 km/h y un kilometraje de 10500 km."
