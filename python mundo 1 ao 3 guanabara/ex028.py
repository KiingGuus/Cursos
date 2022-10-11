import random
esc=int(input('Escolha um numero de 1 a 5: '))
num=[1,2,3,4,5]
mix= random.shuffle(num)
sort=random.choice(num)
if sort== esc:
    print('Voce acertou!!!')
else:
    print('Não foi dessa vez')
print('O numero sorteado foi {}'.format(sort))