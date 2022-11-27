"""
Leia um número fornecido pelo usuário. Se esse número for positivo, culcule a raiz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número
é inválido.
"""
import math
num = int(input(f'Digite um número: '))

if num > 0:
    print(math.sqrt(num))
else:
    print('Número inválido.')

