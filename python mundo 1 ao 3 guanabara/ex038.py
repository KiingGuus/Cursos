a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
if b < a:
    print('O menor numero é {} e o maior numero é {}'. format(b, a))
elif a < b:
    print('O menor numero é {} e o maior numero é {}'.format(a, b))
else:
    print('Os numeros são iguais')
