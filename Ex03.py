#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.
sex = str(input('Digite F ou M:\n').upper().strip())
if sex == 'F' or sex == 'M':
    if sex == 'F':
        print('F = Feminino')
    else:
        print('M = Masculino')
else:
    print('Não é uma resposta valida!!')