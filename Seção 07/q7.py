lista = []

for v in range(10):
    v = int(input('Digite um valor: '))
    lista.append(v)
    print(lista)
    print(max(lista))
    i = lista.index(max(lista))
    print(f'Indice: {i}')