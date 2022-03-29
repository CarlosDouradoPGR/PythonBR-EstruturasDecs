ccc = str(input('Vôce desejas abastecer com Álcool[A] ou Gasolina[A]:\n').upper().strip())
price = float(input('Quantos litros deseja abastecer?\n ').strip())
if ccc in 'AG':
    if ccc == 'A' and price > 20:
        print("Acima de 20 litrs o cliente reebe uma desconto de 5% equivalente a R${}".format(price*5/100))
        print('O valor a ser pago será de R${}'.format(price - price*5/100))
    elif ccc == 'A' and price <= 20:
        print('O posto está dando 3% de desconto em compras até R$20, o que equivale a {}'.format(price*3/100))
        print('O valor a ser pago será de R${}'.format(price - price * 3 / 100))
    elif ccc == 'G' and price > 20:
        print("Acima de 20 litrs o cliente recebe uma desconto de 6% equivalente a R${}".format(price * 6 / 100))
        print('O valor a ser pago será de R${}'.format(price - price * 6 / 100))
    elif ccc == 'G' and price <= 20:
        print('O posto está dando 4% de desconto em compras até R$20, o que equivale a R${}'.format(price*4/100))
        print('O valor a ser pago será de R${}'.format(price - price * 4 / 100))
else:
    print('Valores invalidos')
