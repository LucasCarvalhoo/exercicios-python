"""
Faça um programa que receba dois números e mostre o maior. Se por acaso,
os dois números forem iguais, imprima a mensagem 'números iguais',
"""

num1 = int(input(f'Digite um numero: '))
num2 = int(input(f'Digite outro numero: '))

if num1 > num2:
    print(num1)
if num2 > num1:
    print(num2)
if num1 == num2:
    print('números iguais.')
