from .Carro import Carro

class CarroCorrida(Carro):
  def __init__(self, velocidade):
    super().__init__(velocidade)

  def acelera(self):
    self.velocidade += 15
