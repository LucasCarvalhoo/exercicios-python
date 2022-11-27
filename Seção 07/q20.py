vet = []
impares = []
print('Digite 10 numeros inteiros no intervalo de 0 a 50:')
for i in range(10):

    number = int(input('1 e 10: '))
    if number <= 50:
        vet.append(number)
        if (i % 2 == 0):
            impares.append(number)
    else:
        print('Fora do intervalo!')
tamanho_impar = len(impares)
for i in range(10):
    if i < tamanho_impar:
        print(f' {vet[i]}, {impares[i]}')
    else:
        print(f' {vet[i]}')