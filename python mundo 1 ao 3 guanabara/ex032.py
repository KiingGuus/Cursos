ano=int(input('Digite o ano que gostaria de saber: '))
if ano% 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano BISSEXTO')
else:
    print('O ano não é BISSEXTO')