from classes import Carro
from classes import CarroEsportivo
from classes import CarroInteligente
from classes import CarroPopular
from classes import CarroCorrida

def test_drive(carro):
  print(f"\nTestando {carro.__class__.__name__}: ")
  carro.acelerar()
  carro.exibir_velocidade()

if __name__ == "__main__":
  # carro_inteligente = CarroInteligente(10)
  # print("Carro inteligente: ")
  # carro_inteligente.acelerar()
  # carro_inteligente.exibir_velocidade()
  # carro_inteligente.estacionar()
  # print()

  # carro_esportivo = CarroEsportivo(50)
  # print("Carro Esportivo: ")
  # carro_esportivo.acelerar()
  # carro_esportivo.exibir_velocidade()
  # carro_esportivo.ativar_turbo()
  # carro_esportivo.acelerar()
  # carro_esportivo.exibir_velocidade()
  # carro_esportivo.freiar()
  # carro_esportivo.exibir_velocidade()

  carro_inteligente = CarroInteligente(10)
  carro_inteligente.estacionar()
  test_drive(carro_inteligente)

  carro_corrida = CarroCorrida(70)
  test_drive(carro_corrida)

  

  