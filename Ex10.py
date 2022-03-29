#Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turn = str(input("Olá, digite [M] se seu turno for matutino, [V] se for vespertino ou [N] se for noturno:\n").upper().strip())
if turn == 'M' or turn == 'V' or turn == 'N':
    if turn == 'M' or turn == 'N':
        if turn == 'M':
            print('Bom dia!!')
        else:
            print('Boa noite!!')
    else:
        print('Boa tarde')
else:
    print('Valor inválido!!')
