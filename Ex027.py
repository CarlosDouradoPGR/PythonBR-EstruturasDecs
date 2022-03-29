mca = float(input('Você deseja comprar quantos Kg de maçã: '))
mrg = float(input('Você deseja comprar quantos Kg de morango: '))
if mca <= 5:
    pr_mca = 1.8 * mca
else:
    pr_mca = 1.5 * mca
if mrg <= 5:
    pr_mrg = 2.5 * mrg
else:
    pr_mrg = 2.2 * mrg
somapr = pr_mca + pr_mrg
somakg = mrg + mca
if somakg >= 8 or somapr >= 25:
    print('Acima de R$25 ou 8kg o cliente recebe um desconto de 10% o equivalente a R${:.2f}'.format(somapr*10/100))
    print('O valor a ser pago será de R${:.2f}'.format(somapr - somapr*10/100))
else:
    print('O valor a ser pago será de R${:.2f}'.format(somapr))
