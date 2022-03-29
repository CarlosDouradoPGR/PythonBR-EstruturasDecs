import math


print('Esse programa ira caucular as raízes de uma equação do segundo grau')
print('Sabendo que a equação é do tipo ax2+bx+c informe os valores de:')
a = float(input('a='))
if a == 0:
    print('A equação não é do segundo grau!')
else:
    b = float(input('b='))
    c = float(input('c='))
    disc = b ** 2 - (4 * a * c)
    if disc > 0 and a > 0:
        r1 = -b - (math.sqrt(disc)) / 2 * a
        r2 = -b + (math.sqrt(disc)) / 2 * a
        print('A primeira raíz é {}'.format(r1))
        print('A segunda raíz é {}'.format(r2))
    elif disc == 0:
        print('Possui apenas uma raíz real {}'.format(-b / 2 * a ))
    elif disc < 0:
        print('Não possui raízes reais')





