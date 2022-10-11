from random import randint
itens = ['PEDRA', 'PAPEL', 'TESOURA']
pc = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
player = int(input('Qual sua jogada? '))
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[player]))
if player == 0 and pc == 0 or player == 1 and pc == 1 or player == 2 and pc == 2:
    print('Empate')
elif player == 0 and pc == 1 or player == 1 and pc == 2 or player == 2 and pc == 0:
    print('VOCÊ PERDEU!!!')
elif player == 0 and pc == 2 or player == 1 and pc == 0 or player == 2 and pc == 1:
    print('VOCÊ VENCEU!!!')
