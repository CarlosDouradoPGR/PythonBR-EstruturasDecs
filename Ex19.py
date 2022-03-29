

numb = int(input('Digite um número menor que 1000:\n'))
if numb < 1000:
    und = numb // 1 % 10
    dez = numb // 10 % 10
    cent = numb // 100 % 10
    print('{} possui {} centena'.format(numb, cent))
    print('{} possui {} dezenas'.format(numb, dez))
    print('{} possui {} unidade'.format(numb, und))
else:
    print('Não é um número menor que 1000')
