from .Carro import Carro

class CarroPopular(Carro):
  def __init__(self, velocidade):
    super().__init__(velocidade)
    
  def acelerar(self):
    self.velocidade += 5  
    
  def freiar(self):
    self.velocidade -= 2