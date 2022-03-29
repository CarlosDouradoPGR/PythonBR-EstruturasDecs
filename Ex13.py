D = int(input('Digite um número entre 1 e 7 para encontrar seu correspondete na semana:\n'))
lista = ['0','Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo']

if 1 <= D <= 7:
    print(lista[D])
else:
    print('Número invalido!!')
