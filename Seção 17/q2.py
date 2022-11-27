"""
Baseando-se no exercício 1 adicione um método construtor que permita a definição
de todos os atributos no momento da intanciação do objeto.

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