from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade < 18:
    print('Voce tem {} anos'.format(idade))
    print('Ainda nao pode se alistar, seu alistamento sera no ano de {}'.format(18 - idade + atual))
elif idade == 18:
    print('Voce tem {} anos'.format(idade))
    print('Você deve se alistar esse ano.')
else:
    print('Voce tem {} anos'.format(idade))
    print('Voce deve se alistar imediatamente!!!')
    print('Seu ano de alistamento foi {}'.format(atual - (idade -18)))