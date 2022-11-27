lista = [5, 3, 7, 2, 6, 8, 9, 1]

for i in lista:
    x = int(input(f'Digite um numero de 0 a 7: '))
    print(lista[x])
    y = int(input(f'Digite um numero de 0 a 7: '))
    print(lista[y])
    soma = lista[x] + lista[y]
    print(f'Resultado: {soma}')
    break