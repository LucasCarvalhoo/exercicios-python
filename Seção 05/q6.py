"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre eles.
"""

num1 = int(input(f'Digite um numero: '))
num2 = int(input(f'Digite outro numero: '))

if num1 > num2:
    print(f'{num1}\nDiferença: {num1 - num2}')
else:
    print(f'{num2}\nDiferença: {num2 - num1}')