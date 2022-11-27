"""
Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado.
"""

import math

num = int(input(f'Digite um número: '))
if num > 0:
    print(math.sqrt(num))
else:
    print(math.pow(num, 2))