av1 = float(input('Digite a nota na primeria avaliação:\n'))
av2 = float(input('Digite a nota na segunda avaliação:\n'))
media = ((av1+av2)/2)

if media < 4.0:
    print('Seu conceito é: E')
elif 4 <= media < 6:
    print('Seu conceito é: D')
elif 6 <= media < 7.5:
    print('Seu conceito é: C')
elif 7.5 <= media < 9:
    print('Seu conceito é: B')
elif 9 >= media <= 10:
    print('Seu conceito é: A')
else:
    print('Número invalido')
