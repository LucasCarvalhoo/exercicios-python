
lista = []
def codigo():
    for n in list(range(5)):
        lista.append(int(input('Digite um número: ')))
    codigo = int(input('Ditige o código (0, 1 ou 2): '))
    if codigo == 2:
        lista.reverse()
        print(lista)
    if codigo == 1:
        print(lista)
    if codigo == 0:
        print('código inválido')

codigo()
