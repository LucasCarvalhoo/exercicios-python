"""
Crie uma classe Agenda que pode armazenar 10 pessoas e seja capas de realizar
as seguintes operações:

    - void armazenaPessoa(String nome, int idade, float altura);
    - void removePessoa(String nome);
    - int buscaPessoa(String nome); // informa em que posição da agenda está a
    pessoa
    - void imprimeAgenda(); imprime os dados de todas as pessoas da agenda
    - void imprimePessoa(int index); // imprime os dados da pessoa que está
    na posição "i" da agenda.

"""


class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def mostra_pessoa(self):
        return f'Meu nome é {self.__nome}, tenho {self.__idade} e tenho {self.__altura} de altura'


class Agenda:

    __armazenamento = []

    def armazena_pessoa(self, pessoa):
        if len(self.__armazenamento) < 10:
            self.__armazenamento.append(pessoa)
        else:
            print('Agenda cheia!')

    def remover_pessoa(self, remove_pessoa):
        for pessoa in self.__armazenamento:
            if pessoa.get_nome() == remove_pessoa:
                self.__armazenamento.remove(pessoa)
            print('Pessoa removida!')
            return True
        else:
            print('Pessoa não encontrada!')
            return False
    def busca_pessoa(self, name):
        for pessoa in self.__armazenamento:
            if pessoa.get_nome() == name:
                print(f'A pessoa foi em contrada no indice: {self.__armazenamento.index(pessoa)}')
                return True
            else:
                print('Pessoa não encontrada')
                return False

    def imprimir_agenda(self):
        for pessoa in self.__armazenamento:
            print(f'Nome: {Pessoa.get_nome(pessoa)}')
            print(f'Idade: {Pessoa.get_idade(pessoa)}')
            print(f'Altura; {Pessoa.get_altura(pessoa)}\n')

    def imprimir_dados(self, posicao):
        if 0 <= posicao <= len(self.__armazenamento):
            lista = self.__armazenamento
            pessoa = lista[posicao]
            print(f'Nome: {Pessoa.get_nome(pessoa)}')
            print(f'Idade: {Pessoa.get_idade(pessoa)}')
            print(f'Altura: {Pessoa.get_altura(pessoa)}')

p1 = Pessoa('Lucas', 20, 1.75)
p2 = Pessoa('Lorena', 16, 1.60)

colecao_pessoa = [p1, p2]
agenda = Agenda()

for pessoa in colecao_pessoa:
    Agenda.armazena_pessoa(agenda, pessoa)


Agenda.imprimir_agenda(agenda)