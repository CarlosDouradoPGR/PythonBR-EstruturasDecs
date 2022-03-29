#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
word = str(input('Digite uma letra para saber se é vogal ou consante:\n').lower())

if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
    print('Vogal')
else:
    print('Consoante')
