"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""

first = int(input(f'Digite o primeiro número: '))
second = int(input(f'Digite o segundo número: '))

if first > second:
    print(f'{first} é maior que {second}')
else:
    print(f'{second} é maoir que {first}')