saque = int(input('Digite o valor para saque:\n'))
n100 = saque // 100
n50 = saque // 10 % 10
n1 = saque // 1 % 10
n5 = n1 // 5


print(n100, n50, n1)

if n100 < 6:
    print('Serão usadas {} nota de R$100'.format(n100))
    if 5 <= n50 < 10:
        if n50 > 5:
            print('Serão usadas 1 nota de R$50')
            print('Serão usadas {} notas de R$10'.format(n50 - 5))
        else:
            print('Serão usadas 1 nota de R$50')
    if 5 > n50 > 0:
        print('Serão usadas {} notas de R$10'.format(n50))
    if 5 > n1 > 0:
        print('Serão usadas {} notas de R$1'.format(n1))
    if 10 > n1 > 5:
        print('Serão usadas 1 nota de R$5')
        print('Serão usadas {} notas de R$1'.format(n1-5))
else:
    print('Não é possivel sacar esse valor')


