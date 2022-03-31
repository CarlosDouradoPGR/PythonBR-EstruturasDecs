choice = str(input('Digite [FD] para file duplo\n'
                   'Digite [A] para alcatra\n'
                   'Digite [P] para picanha\n').upper().strip())
if choice == "FD" or choice == 'P' or choice == 'A':
    kg = float(input('Digite a quantidade de Kg de carne: '))
    card = str(input('Deseja pagar com o cartão Tabajara?[S/N]:\n').upper().strip())
    if choice == 'FD':
        carn = 'FILE DUPLO'
        if kg > 5:
            v = 5.8
            price = v * kg
        else:
            v = 4.9
            price = v * kg
    if choice == 'A':
        carn = 'ALCATRA'
        if kg > 5:
            v = 6.8
            price = v * kg
        else:
            v = 5.9
            price = v * kg
    if choice == 'P':
        carn = 'PICANHA'
        if kg > 5:
            v = 7.8
            price = v * kg
        else:
            v = 6.9
            price = v * kg

    if card == 'S':
        desc = price * 5/100
    elif card == 'N':
        desc = 'SEM DESCONTO'
    if card == 'N':
        print(20*'-', 'NOTA FISCAL','-'*20)
        print('Peça de carne: {}'.format(carn))
        print('Valor R${:.2f} pro Kg'.format(v))
        print('Forma de pagamento: DINHEIRO')
        print('Desconto no cartão Tabajara:{}'.format(desc))
        print('Valor a pagar R${:.2f}'.format(price))
        print(40*'-')
    elif card == 'S':
        print(20 * '-', 'NOTA FISCAL', '-' * 20)
        print('Peça de carne: {}'.format(carn))
        print('Valor R${:.2f} por Kg'.format(v))
        print('Forma de pagamento: CARTÃO')
        print('Desconto no cartão Tabajara: {}'.format(desc))
        print('Valor a pagar R${:.2f}'.format(price-desc))
        print(54 * '-')
else:
    print('Valor invalido')
