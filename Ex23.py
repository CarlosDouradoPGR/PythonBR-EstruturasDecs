import math

numb = float(input('Digite um número para saber se ele é inteiro ou decimal:\n'))
print(math.ceil(numb))
if math.ceil(numb) > numb:
    print('É decimal')
else:
    print('É inteiro')

