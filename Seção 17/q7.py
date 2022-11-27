"""
Escreva um código que apresenta a classe Circulo, com atributos raio,
área e périmetro e, os métodos calcularArea, calcularPerimetro e imprimir. Os
métodos calcularArea e calcularPerimetro devem efetuar seus respectivos
cálculos e colocar os valores nos atrubutos area e perimetro. O método imprimir
dece mostrar na tela os valores de todos os atributos. Salienta-se que a área de
um circulo é obtida pela fórmula (pi * raio * raio) e o perímetro por (2 * pi *
raio), omde pi = 3,141516.

"""
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.area = (math.pi * raio * raio)
        self.perimetro = (2 * math.pi * raio)

    @property
    def imprimir(self):
        return f'Raio: {self.raio}\nÁrea: {self.area:,.2f}\nPérimetro: {self.perimetro:,.2f}'


# Teste

circulo1 = Circulo(5)
print(circulo1.imprimir)