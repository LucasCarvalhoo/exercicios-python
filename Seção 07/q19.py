lista = []
n = 50
for i in range(0, n, 1):
    lista.append((i + 5 * i) % (i + 1))

print(lista)