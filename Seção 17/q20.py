"""
Escreva um código que apresente a classe Televisor, com atributos ligado, canal e volume
e, o método imprimir. O atributo ligado será boleano e deverá indicar o estado atual do
televisor, se ligado ou desligado. O atributo canal deverá indicar o canal atual em que o
televisor está sintonizado. O atributo volume deverá indicar o volume atual do televisor.
"""

class Televisor:
    def __init__(self, canal, numeroCanais, volume, volumeMaximo, ligada=False):
        self.__canal = canal
        self.__numeroCanais = numeroCanais
        self.__volume = volume
        self.__volumeMaximo = volumeMaximo
        self.__ligada = ligada

    def liga_desliga(self):
        self.__ligada = not self.__ligada
        if self.__ligada:
            return f'A TV está ligada no canal {self.__canal}'
        else:
            return 'A TV está desligada'

    def acima_canal(self):
        if self.__canal < self.__numeroCanais:
            self.__canal += 1
            return f'Está no canal {self.__canal}'
        elif self.__canal == self.__numeroCanais:
            return f'Está no canal {1}'

    def abaixo_canal(self):
        if self.__canal < self.__numeroCanais:
            if self.__canal > 0:
                self.__canal -= 1
                return f'Está no canal {self.__canal}'
            elif self.__canal <= 0:
                return f'Está no canal {self.__numeroCanais}'

    def aumentar_volume(self):
        self.__volume += 1
        return f'Está no volume {self.__volume}'

    def diminuir_volume(self):
        self.__volume -= 1
        return f'Está no volume {self.__volume}'

    def mostra_info(self):
        if self.__ligada:
            return f'A TV está ligada no canal {self.__canal} ' \
                   f'no volume {self.__volume}'
        else:
            return 'A TV está desligada'


# Teste
televisao = Televisor(5, 10, 2, 10)

print(televisao.mostra_info())

print(televisao.liga_desliga())
print(televisao.mostra_info())