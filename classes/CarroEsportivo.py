from .Carro import Carro

class CarroEsportivo(Carro):
  def __init__(self, velocidade):
    super().__init__(velocidade)

    self.turbo = False

  def acelerar(self):
    if self.turbo:
      self.velocidade += 10
    else:
      self.velocidade += 5
    
  def freiar(self):
    self.velocidade -= 2

  def ativar_turbo(self):
    if self.turbo:
      self.turbo = False
    else:
      self.turbo = True

    print("Turbo ativado! A aceleração duplicou")