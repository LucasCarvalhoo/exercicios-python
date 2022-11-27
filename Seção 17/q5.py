"""
Escreva um código que apresente a classe retângulo, com atributos comprimento, largura, área e perímetro e, os métodos
calcularArea, calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro devem efetuar seus respectivos
cálculos e colocar os valores nos atributos area e perimetro. O método imprimir deve mostra na tela os valores de todos
os atributos. Salienta-se que a área de um retângulo é obtida pela fórmula (comprimento * largura) e o perímetro por
(2 * comprimento) + (2 * largura).

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