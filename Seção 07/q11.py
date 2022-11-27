lista = [15, 17, -5, 4, -42, 5, 2, 6, 66, 10]

pos = 0
neg = 0
soma_dos_positivos = 0
for num in lista:
    if num > 0:
        pos += 1
        soma_dos_positivos += num
    else:
        neg += 1


print(f'Numeros negativos: {neg}')

"""
Não utilizar o sum, pois ele soma elementos iteraveis. Em vez disso somar o valor de cada numeros a essa
variavel (inicializada por zero) faz mais sentido.

Está aqui seria a forma pythonica de escrever o código:

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
soma_dos_negativos = sum(n for n in lista if n < 0)
print('A soma dos elementos negativos é igual a {}'.format(soma_dos_negativos))


"""
print(f'A soma dos numeros positivos é: {soma_dos_positivos}')






