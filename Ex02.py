#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
numb = int(input('Digite um número inteiro para saber se é positivo ou negativo:\n'))
if numb >=1:
    print('{} é positivo!!'.format(numb))
else:
    print('{} é negativo ou nulo'.format(numb))

