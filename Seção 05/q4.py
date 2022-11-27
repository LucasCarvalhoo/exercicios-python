"""
Faça um programa que leia um número e, caso ele seja positico, calcule e mostre:
    - O número digitado ao quadrado;
    - A raiz quadrada do número digitado;
"""
import math

num = int(input(f'Digite um numero: '))

if num > 0:
    print(f'O quadrado de {num} é {math.pow(num, 2)}\nE a raiz quadrada de {num} é {math.sqrt(num)}')
else:
    print('Número invalido.')