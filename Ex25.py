print('Interrogando um suspeito: ')
pg1 = str(input("Telefonou para a vítma?(S/N)\n").upper().strip())
pg2 = str(input('Esteve no local do crime?(S/N)\n').upper().strip())
pg3 = str(input('Mora perto da vítma?(S/N)\n').upper().strip())
pg4 = str(input('Devia para a vítma?(S/N)\n').upper().strip())
pg5 = str(input('Já trabalhou com a vítma?(S/N\n').upper().strip())
lst = [pg1, pg2, pg3, pg4, pg5].count('S')

if 3 > lst >= 2 :
    print('Suspeita')
elif lst == 3 or lst == 4:
    print('Cúmplice')
elif lst == 5:
    print('Assassino')
else:
    print('Inocente')

