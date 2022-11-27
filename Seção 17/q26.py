"""
Escreva um código que apresente a classe Microondas, com atributo
ligado e o método imprimir. O método imprimir deve mostrar na tela
os valores de todos os atributos. O atributo ligado será boleano e
deverá indicar o estado atual do microondas, se ligado ou desligado.

"""
class Microondas:
    def __init__(self, ligado=True, portaFechada=True):
        self.__ligado = ligado
        self.__portaFechada = portaFechada

    def liga_desliga(self):
        self.__ligado = not self.__ligado
        if self.__ligado:
            if self.__portaFechada == True:
                return 'Microondas Ligado'
            elif self.__portaFechada == False:
                return 'Porta aberta, feche a porta para ligar o microondas'
        else:
            return 'Microondas Desligado'

    def abre_fecha(self):
        self.__portaFechada = not self.__portaFechada
        if self.__portaFechada:
            return 'Porta Fechada'
        else:
            return 'Porta Aberta'

    def mostra_info(self):
        if self.__ligado:
            return f'Microondas Ligado'
        else:
            return 'Microondas Desligado'



# Teste

microondas = Microondas()
print(microondas.mostra_info())
print(microondas.abre_fecha())
print(microondas.liga_desliga())
print(microondas.liga_desliga())
print(microondas.liga_desliga())
print(microondas.abre_fecha())
print(microondas.liga_desliga())
print(microondas.mostra_info())