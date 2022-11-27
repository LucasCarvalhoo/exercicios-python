"""
Crie uma classe para representar um pessoa, com os atributos privados de nome,
idade, altura. Crie os métodos públicos necessários para sets e gets e também
um método para imprimir os dados de uma pessoa.
"""

class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def altura(self):
        return self.__altura

    @property
    def mostra_pessoa(self):
        return f'Meu nome é {self.__nome}, tenho {self.__idade} anos e tenho {self.__altura} de altura'

p1 = Pessoa('Lucas', 20, 1.75)
print(p1.mostra_pessoa)
