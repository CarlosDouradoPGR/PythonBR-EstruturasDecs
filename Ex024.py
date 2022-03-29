import math

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
op = int(input('Digite [1] para somar\n'
               'Digite [2] para subtrair\n'
               'Digite [3] para multiplicar\n'
               'Digite [4] para dividir\n'))
soma = n1+n2
subt = n1-n2
mult = n1*n2
div = n1/n2

if op == 1:
    print('O resultado é {}'.format(n1 + n2))
    if (n1+n2) % 2 == 0:
        print('É par')
    else:
        print('É impar')
    if math.ceil(n1+n2) > n1+n2:
        print('É decimal')
    else:
        print('É inteiro')
    if (n1+n2) > 0:
        print('É positivo')
    elif (n1+n2) == 0:
        print('Neutro')
    elif (n1+n2) < 0:
        print('Negativo')
if op == 2:
    print('O resultado é {}'.format(subt))
    if subt % 2 == 0:
        print('É par')
    else:
        print('É impar')
    if math.ceil(subt) > subt:
        print('É decimal')
    else:
        print('É inteiro')
    if subt > 0:
        print('É positivo')
    elif subt == 0:
        print('Neutro')
    elif subt < 0:
        print('Negativo')
if op == 3:
    print('O resultado é {}'.format(mult))
    if mult % 2 == 0:
        print('É par')
    else:
        print('É impar')
    if math.ceil(mult) > mult:
        print('É decimal')
    else:
        print('É inteiro')
    if mult > 0:
        print('É positivo')
    elif mult == 0:
        print('Neutro')
    elif mult < 0:
        print('Negativo')
if op == 4:
    print('O resultado é {}'.format(div))
    if div % 2 == 0:
        print('É par')
    else:
        print('É impar')
    if math.ceil(div) > n1+n2:
        print('É decimal')
    else:
        print('É inteiro')
    if div > 0:
        print('É positivo')
    elif div == 0:
        print('Neutro')
    elif div < 0:
        print('Negativo')


