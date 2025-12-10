class Carro:
  def __init__(self, velocidade):
    self.velocidade = velocidade

  def acelerar(self):
    self.velocidade += 1

  def freiar(self):
    self.velocidade -= 1

  def exibir_velocidade(self):
    print(f"A velocidade atual é de: {self.velocidade} km/h")