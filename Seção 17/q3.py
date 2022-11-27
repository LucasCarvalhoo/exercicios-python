"""
Escreva um código que apresente a classe Quadrado, com atributos lado, área
e perímetro e, os métodos calcularArea, calcularPerimetro e imprimir.
Os métodos e calcularArea e calcularPerimetro devem efetuar seus respectivos
calculos e colocar os valores nos atributos area e perimetro. O método imprimir
deve mostrar na tela os valores de todos os atributos. Salienta-se que a área de
um quadrado é obtida pela formula (lado * lado) e o perímetro por (4 * lado).

"""

class Quadrado:
    def __init__(self, lado):
        self.__lado = lado
        self.__area = (self.__lado * self.__lado)
        self.__perimetro = (self.__lado * 4)

    @property
    def imprimir(self):
        return f'Lados: {self.__lado}\nÁrea: {self.__area}\nPerímetro: {self.__perimetro}'

# Teste

quadrado1 = Quadrado(8)
print(quadrado1.imprimir)