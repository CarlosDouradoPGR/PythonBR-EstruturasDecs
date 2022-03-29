#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
print('Digite o valor de 3 produtos para descobrir qual é o mais barato')

p1 = float(input('Digite o valor de um produto: '))
p2 = float(input('Digite o valor de outro produto: '))
p3 = float(input('Digite o valor de outo produto: '))
lista = [p1, p2, p3]
lista.sort(reverse=True)
print('O produto recomendado para a compra é o {}'.format(lista[2]))

