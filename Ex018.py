import datetime

#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
print('Digite uma data')
d = int(input('Digite o dia: '))
m = int(input('Digite o mês: '))
a = int(input('Digite o ano: '))
if 0 < d <= 31 and 0 < m <= 12 and a > 0:
    print('A data é {}/{}/{}'.format(d, m, a))
else:
    print('Não é uma data valida')



