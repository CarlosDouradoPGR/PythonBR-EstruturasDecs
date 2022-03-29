#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

wage = float(input('Olá, por favor, digite o seu salário atual: \nR$'))
if wage > 0 or wage < 1500.00:
    if wage < 700.00:
        if wage < 280 :
            print('Salário antes do reajuste: {:.2f}'.format(wage))
            print('Percentual de aumento aplicado: 20%')
            print('Valo do aumento: {:.2f}'.format(wage*20/100))
            print('Seu salário será de R${:.2f}'.format((wage * 20 / 100) + wage))
        else:
            print('Salário antes do reajuste: {:.2f}'.format(wage))
            print('Percentual de aumento aplicado: 15%')
            print('Valo do aumento: {:.2f}'.format(wage * 15 / 100))
            print('Seu salário será de R${:.2f}'.format((wage*15/100)+wage))
    else:
        print('Salário antes do reajuste: {:.2f}'.format(wage))
        print('Percentual de aumento aplicado: 10%')
        print('Valo do aumento: {:.2f}'.format(wage * 10 / 100))
        print('Seu salário será de ${:.2f}'.format((wage*10/100)+wage))
else:
    print('Salário antes do reajuste: {:.2f}'.format(wage))
    print('Percentual de aumento aplicado: 5%')
    print('Valo do aumento: {:.2f}'.format(wage * 5 / 100))
    print('Seu salário será de R${:.2f}'.format(wage*5/100+wage))