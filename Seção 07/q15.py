


lista = [20, 30, 15, 14, 54, 54, 13, 12, 45, 31, 20, 14, 56, 15, 62, 23, 14, 54, 10, 30]

print(sorted(set(lista))) # Lista ordernada com retirada dos numeros repetidos
# No caso do sort, não funciona


# OR

from collections import OrderedDict

lista2 = [20, 30, 15, 14, 54, 54, 13, 12, 45, 31, 20, 14, 56, 15, 62, 23, 14, 54, 10, 30]
print(list(OrderedDict.fromkeys(lista2))) # Retirada dos numeros repetidos

# OR




