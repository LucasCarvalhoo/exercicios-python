"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas
e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente,
um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato
deve ser informado ao usuário e o programa termina.
"""

nota1 = int(input(f'Digite a primeria nota: '))
nota2 = int(input(f'Digite a segunda nota: '))
notas = []
notas.append(nota1)
notas.append(nota2)

if (nota1 and nota2 >= 0) and (nota1 and nota2 <= 10):
    print('nota válida')
    print(sum(notas) / len(notas))
else:
    print('nota inválida')



