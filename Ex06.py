#Faça um Programa que leia três números e mostre o maior deles.
import math

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
lista = [n1, n2, n3]
lista.sort(reverse=True)
print('O maior número é {}'.format(lista[0]))
