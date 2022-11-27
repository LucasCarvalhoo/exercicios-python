"""
Escreva um código que apresente a classe Moto, com atributos marca, modelo, cor e marcha e, o método imprimir.
O método imprimir deve mostrar na tela os valores de todos os atributos. O atributo marcha indica em que a marcha
a Moto se encontra no momento, sendo representado de forma inteira, onde 0 - neutro, 1 - primeira, 2 - segunda, etc.
"""

class Moto:

    __marchas = {0: 'Neutra', 1: 'Primeira', 2: 'Segunda', 3: 'Terceira', 4: 'Quarta', 5: 'Quinta'}
    def __init__(self, marca, modelo, cor, marcha=0, ligada=False):
        self.__ligada = ligada
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__num_marcha = marcha
        self.__marcha = Moto.__marchas[marcha]

    def liga_desliga(self):
        self.__ligada = not self.__ligada
        if self.__ligada:
            return 'A moto está ligada'
        else:
            return 'A moto está desligada'

    def passar_marcha(self):
        if self.__ligada:
            if self.__num_marcha < 5:
                self.__marcha = Moto.__marchas[self.__num_marcha + 1]
                self.__num_marcha += 1
                return f'A moto passou uma marcha e está na {self.__marcha} marcha'
            else:
                return 'A moto está na quinta marcha'
        else:
            return 'A moto está desligada'

    def voltar_marcha(self):
        if self.__ligada:
            if self.__num_marcha > 0:
                self.__marcha = Moto.__marchas[self.__num_marcha - 1]
                self.__num_marcha -= 1
                return f'A moto voltou uma marcha e está na {self.__marcha} marcha'
            else:
                return f'A moto está na marcha {self.__marcha}'
        else:
            return 'A moto está desligada'

    def mostra_info(self):
        if self.__ligada:
            return f'A moto da marca {self.__marca} e modelo {self.__modelo} da cor {self.__cor} está na marcha {self.__marcha}'
        else:
            return 'A moto está desligada'
# Teste

moto1 = Moto('Honda', 'Bros', 'vermelha')
print(moto1.mostra_info())
print(moto1.liga_desliga())
print(moto1.mostra_info())


