#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

wage = float(input('Por favor digite o seu salário:\n'))
sind = (wage*3/100)
fgts = (wage*11/100)
if wage > 0 and wage < 2500.00:
    if wage <= 1500:
        if wage <= 900:
            print('Salário bruto = R${:.2f}'.format(wage))
            print('(-) Imposto de renda = Insento')
            print('(-) INSS (10%) = {:.2f}'.format((wage * 10 / 100) + wage))
            print('FGTS (11%): R${:.2f}'.format((wage * 11 / 100) + wage))
            print('Total de descontos = R${:.2f}'.format(wage * 10 / 100))
            print('Salário liquido: {:.2f'.format(wage - (wage * 10 / 100)))
        else:
            print('Salário bruto = R${:.2f}'.format(wage))
            print('(-) Imposto de renda (5%) = {:.2f}'.format(wage*5/100))
            print('(-) INSS (10%) = {:.2f}'.format((wage * 10 / 100) ))
            print('FGTS (11%): R${:.2f}'.format((wage * 11 / 100)))
            print('Total de descontos = R${:.2f}'.format(wage * 5/100 + wage * 10 / 100))
            print('Salário liquido = R${:.2f}'.format(wage - (wage*5/100 + wage * 10 / 100)))
    else:
        print('Salário bruto = R${:.2f}'.format(wage))
        print('(-) Imposto de renda (10%) = R${:.2f}'.format((wage * 10 / 100) + wage))
        print('(-) INSS (10%) = {:.2f}'.format((wage * 10 / 100) + wage))
        print('FGTS (11%) = R${:.2f}'.format((wage * 11 / 100) + wage))
        print('Total de descontos = R${:.2f}'.format(wage * 10 / 100 + wage * 10 / 100))
        print('Salário liquido: {}'.format(wage - (wage * 10/ 100 + wage * 10 / 100)))

else:
    print('Salário bruto = R${}'.format(wage))
    print('(-) Imposto de renda (20%) = R${}'.format((wage*20/100)+wage))
    print('(-) INSS (10%) = R${:.2f}'.format((wage*10/100) + wage))
    print('FGTS (11%): R${:.2f}'.format((wage*11/100) + wage))
    print('Total de descontos = R${:.2f}'.format(wage*20/100+wage*10/100))
    print('Salário liquido = R${:.2f}'.format(wage-(wage*20/100 + wage*10/100)))
