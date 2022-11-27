lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def multiplos():
    x = int(input('Digite um número: '))
    for i in lista:
        if i % x == 0:
            print(i)


multiplos()