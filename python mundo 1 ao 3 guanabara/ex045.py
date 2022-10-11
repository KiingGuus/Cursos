import random
player = int(input('''Selecione a opção:
[1] PEDRA
[2] PAPEL
[3] TESOURA
OPÇÃO: '''))
playere = 0
if player == 1:
    playere = 'PEDRA'
elif player == 2:
    playere = 'PAPEL'
elif player == 3:
    plaere = 'TEROURA'
lista= ['PEDRA','PAPEL','TESOURA']
embaralho= random.shuffle(lista)
pc = random.choice(lista)
if player == 1 and pc =='PEDRA' or player == 2 and pc == 'PAPEL' or player == 3 and pc == 'TESOURA':
    print('''Empate
O computador escolheu {} e você escolheu {}'''.format(pc, playere))
elif player == 1 and pc == 'PAPEL' or player == 2 and pc == 'TESOURA' or player == 3 and pc == 'PEDRA':
    print('''VOCÊ PERDEU!!!.'
O computador escolheu {} e você escolheu {}'''.format(pc, playere))
elif player == 1 and pc == 'TESOURA' or player == 2 and pc == 'PEDRA' or player == 3 and pc == 'PAPEL':
    print('''VOCÊ VENCEU!!!.
O computador escolheu {} e você escolheu {}'''.format(pc, playere))
else:
    print('Opção invalida')