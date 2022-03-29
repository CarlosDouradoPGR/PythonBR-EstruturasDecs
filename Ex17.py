#Faça um Programa que peça um número correspondente a um determinado ano
# e em seguida informe se este ano é ou não bissexto.

yrs = int(input('Digite um ano para saber se ele é bissexto ou não:\n'))
if yrs % 4 == 0:
    print('É bissexto')
else:
    print('Não é bissexto')
