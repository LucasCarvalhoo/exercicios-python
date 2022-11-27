"""
Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o
volume e trocar os canais da televisão.

    - O controle de volume permite aumentar ou diminuir a potência do volume de
    som em uma unidade de cada vez;
    - O controle de canal também permite aumentar e diminuir o número do canal
    em uma unidade, porém, também possibilita trocar para um canal indicado;
    - Também devem existir métodos para consultar o valor do volume de som e o
    canal selecionado.
"""
# metodos: aumentaVolume, diminuiVolume, mostraVolume, aumentaCanal, diminuiCanal, mostraCanal
# atributos:
class Televisao:
    def __init__(self, canal=10, volume=0):
        self.__canal = canal
        self.volume = volume

class ControleRemoto:
    def __init__(self):
        pass


    def aumentaVolume(self):
        self.volume += 1

    def diminuiVolume(self):
        self.volume -= 1

    def mostraVolume(self):
        print(f'Volume {self.volume}')

    def aumentaCanal(self):
        self._Televisao__canal += 1

    def diminuiCanal(self):
        self._Televisao__canal -= 1

    def mostaCanal(self):
        print(f'Canal {self._Televisao__canal}')

televisao = Televisao()

ControleRemoto.aumentaVolume(televisao)
ControleRemoto.aumentaVolume(televisao)
ControleRemoto.aumentaVolume(televisao)
ControleRemoto.aumentaVolume(televisao)
ControleRemoto.aumentaVolume(televisao)
ControleRemoto.aumentaVolume(televisao)
ControleRemoto.aumentaVolume(televisao)
ControleRemoto.aumentaVolume(televisao)
print(televisao.__dict__)
ControleRemoto.aumentaCanal(televisao)
print(televisao.__dict__)
# ControleRemoto.diminuiCanal(televisao)
# print(televisao.__dict__)
# ControleRemoto.diminuiVolume(televisao)
# print(televisao.__dict__)


ControleRemoto.mostaCanal(televisao)
ControleRemoto.mostraVolume(televisao)

