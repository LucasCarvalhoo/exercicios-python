"""
Crie uma classe denominada Elevador para armazenar as informações de um elevador
dentro de um prédio. A classe deve armazenar o ardar atual (térreo = 0), total de
andares do prédio, exluindo o térreo, capacidade do elevador, e quantas pessoas estão
presentes nele.

A classe deve também disponibilizar os seguintes métodos:

    - inicializa: que deve receber como parâmetros a capacidade do elevador e o
    total de andares no prédio (os elevadores sempre começam no térreo e vazio);
    - entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ain-
    da houver espaço);
    - sai: para remover uma pessoa do elevador (só deve remover se houver alguém
    dentro dele);
    - desce: para descer um andar (não deve descer se já estiver no térreo);
    - encapsular todos os atributos da classe (criar os set e get).
"""
# classe: elevador
# Atributos: andarAtual, andaresPredio, capacidadeDoElevador, quantidadePessoas
# Métodos: inicializa, entra, sai, desce.
class Elevador:
    def __init__(self, andaresPredio=0, andarAtual=0, capacidadeMaxima=0, quantidadePessoa=0):
        self.__andarAtual = andarAtual
        self.__andaresPredio = andaresPredio
        self.__capacidadeMaxima = capacidadeMaxima
        self.__quantidadePessoa = quantidadePessoa

    def inicializar(self, andaresPredio, capacidadeMaxima):
        self.__init__(andaresPredio, 0, capacidadeMaxima, 0)

    def entrar(self):
        if self.__quantidadePessoa < self.__capacidadeMaxima:
            self.__quantidadePessoa += 1
        else:
            return f'Esta lotado!'

    def sair(self):
        if self.__quantidadePessoa > 0:
            self.__quantidadePessoa -= 1

    def subir(self):
        if self.__andarAtual < self.__andaresPredio:
            self.__andarAtual += 1
        else:
            return f'O elevador se encontra no ultimo andar.'

    def descer(self):
        if self.__andarAtual > 0:
            self.__andarAtual -= 1
        else:
            return f'O elevador se encontra no terreo.'

    @property
    def andaresPredio(self):
            return self.__andaresPredio

    @andaresPredio.setter
    def andaresPredio(self, andaresPredio):
        self.__andaresPredio = andaresPredio

    @property
    def andarAtual(self):
        return self.__andarAtual

    @andarAtual.setter
    def andarAtual(self, andarAtual):
        self.__andarAtual = andarAtual

    @property
    def capacidadeMaxima(self):
        return self.__capacidadeMaxima

    @capacidadeMaxima.setter
    def capacidadeMaxima(self, capacidadeMaxima):
        self.__capacidadeMaxima = capacidadeMaxima

    @property
    def quantidadePessoa(self):
        return self.__quantidadePessoa

    @quantidadePessoa.setter
    def quantidadePessoa(self, quantidadePessoa):
        self.__quantidadePessoa = quantidadePessoa

elevador = Elevador()
elevador.inicializar(7, 8)

elevador.entrar()
print(vars(elevador))
elevador.entrar()
print(vars(elevador))
elevador.entrar()
print(vars(elevador))
elevador.subir()
print(vars(elevador))
elevador.subir()
print(vars(elevador))
elevador.sair()
print(vars(elevador))
elevador.entrar()
print(vars(elevador))
elevador.entrar()
print(vars(elevador))
