"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se o a prestação for maior que 20% do salário imprima: 'emprestimo não consedido',
caso contrario imprima 'emprestimo concedido'.
"""

salario = 1250
prestacao = 200
if prestacao > (salario * 0.2):
    print('emprestimo não consedido')
else:
    print('emprestimo concedido')
