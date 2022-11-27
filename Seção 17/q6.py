"""
Baseando-se no exercício 5 adicione um método construtor que permita
a definição de todos os atributos no momento da intanciação do objeto.

"""

class Retangulo:
    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura
        self.__area = (comprimento * largura)
        self.__perimetro = (2 * comprimento) + (2 * largura)

    @property
    def imprimir(self):
        return f'Comprimento: {self.__comprimento}\nLargura: {self.__largura}\nÁrea: {self.__area}\nPerímetro: {self.__perimetro}'


# Teste

retangulo1 = Retangulo(8, 10)
print(retangulo1.imprimir)