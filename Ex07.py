#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
lista = [n1, n2, n3]
lista.sort(reverse=True)
print('O maior número entre eles é {} e o menor é {}'.format(lista[0], lista[2]))
