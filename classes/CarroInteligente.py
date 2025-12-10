from .Carro import Carro

class CarroInteligente(Carro):
  def __init__(self, velocidade):
    super().__init__(velocidade)

  def estacionar(self):
    print("Estacionando automaticamente...")