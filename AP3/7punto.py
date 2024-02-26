class CuentaBancaria:
  """
  Clase que representa una cuenta bancaria.
  """

  def __init__(self, numero_cuenta, propietarios, balance):
    """
    Inicializa una nueva cuenta bancaria.

    Args:
      numero_cuenta (str): El número de la cuenta bancaria.
      propietarios (list): Lista de nombres de los propietarios de la cuenta.
      balance (float): El balance actual de la cuenta.
    """
    self.numero_cuenta = numero_cuenta
    self.propietarios = propietarios
    self.balance = balance

  def __str__(self):
    """
    Devuelve una representación textual de la cuenta bancaria.

    Returns:
      str: Una cadena que describe la cuenta bancaria.
    """
    return f"Cuenta bancaria {self.numero_cuenta} con balance {self.balance:.2f}€"


cuenta_bancaria = CuentaBancaria("ES1234567890", ["Juan Pérez", "Ana López"], 1000.50)
print(cuenta_bancaria)  
