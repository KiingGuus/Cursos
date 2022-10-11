from random import randint
itens = ['PEDRA', 'PAPEL', 'TESOURA']
pc = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
if pc == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('DERROTA')
    else:
        print('JOGADA INVALIDA')
elif pc == 1: #papel
    if jogador == 0:
        print('PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif pc == 2: #tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

