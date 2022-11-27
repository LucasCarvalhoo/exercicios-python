"""
Baseando-se no exercício 3 adicione um método construtor que permita a definição de todos os
atributos no momento da instanciação do objeto.

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