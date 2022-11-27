"""
Escreva um código que apresenta a classe Pessoa, com atributos nome, endereço e telefone e, o método imprimir.
O método imprimir deve mostrar na tela os valores de todos os atributos.

"""

class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def imprimir(self):
        return f'Nome: {self.__nome}\nEndereço: {self.__endereco}\nTelefone: {self.__telefone}'


# Teste

contato1 = Pessoa('Lucas', 'Rua São José, 22', 21940028922)
print(contato1.imprimir)