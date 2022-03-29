print("Faça um Programa que leia três números e mostre-os em ordem decrescente.")
print('Digite 3 números')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outo número: '))
n3 = float(input('Mais um número: '))
lista = [n1, n2, n3]
lista.sort()
print(lista)