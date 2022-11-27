"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule
e mostre o peso ideal, utilizando as seguites fórmulas (onde h corresponde à altura):
    - Homens: (72.7 * h) -  58
    - Mulheres: (62.1 * h) - 44.7
"""
sexo = input('Digite M ou F: ')
h = float(input('Qual sua altura(em metros)? '))
if sexo == "M":
    peso = (72.7 * h) - 58
if sexo == "F":
    peso = (62.1 * h) - 44.7
print(f'O peso ideal é {peso:.2f}kg.')