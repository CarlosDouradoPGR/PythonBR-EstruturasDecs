#Faça um Programa que peça dois números e imprima o maior deles.
print('\033[4m Digite dois número para saber qual dele é o maior\033[4m')
n1 = int(input('\033[0;34mDigite um número:\n\033[0;34m'))
n2 = int(input('\033[0;31mDigite outro número:\n\033[0;31m'))
if n1 > n2:
    print('{} é o maior'.format(n1))
else:
    print('{} é maior'.format(n2))