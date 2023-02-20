from random import randint

def jogada_computador():
    return itens[randint(0, 2)]

def jogada_jogador():
    jogada = int(input('Qual sua jogada? '))
    if jogada not in [0, 1, 2]:
        print('Jogada inválida')
        return None
    return itens[jogada]

def resultado(jogada_pc, jogada_jogador):
    if jogada_pc == 'PEDRA':
        if jogada_jogador == 'PEDRA':
            return 'EMPATE'
        elif jogada_jogador == 'PAPEL':
            return 'JOGADOR VENCEU'
        elif jogada_jogador == 'TESOURA':
            return 'DERROTA'
    elif jogada_pc == 'PAPEL':
        if jogada_jogador == 'PEDRA':
            return 'DERROTA'
        elif jogada_jogador == 'PAPEL':
            return 'EMPATE'
        elif jogada_jogador == 'TESOURA':
            return 'JOGADOR VENCEU'
    elif jogada_pc == 'TESOURA':
        if jogada_jogador == 'PEDRA':
            return 'JOGADOR VENCEU'
        elif jogada_jogador == 'PAPEL':
            return 'DERROTA'
        elif jogada_jogador == 'TESOURA':
            return 'EMPATE'

itens = ['PEDRA', 'PAPEL', 'TESOURA']
turns = int(input("Quantas partidas você deseja jogar? "))
turn = 0
win = 0
lose = 0

while turn < turns:
    print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
    jogada_jogador = jogada_jogador()
    if jogada_jogador is None:
        continue
    jogada_pc = jogada_computador()
    print('Computador jogou {}'.format(jogada_pc))
    print('Jogador jogou {}'.format(jogada_jogador))
    resultado_jogo = resultado(jogada_pc, jogada_jogador)
    print(resultado_jogo)
    if resultado_jogo == 'JOGADOR VENCEU':
        win += 1
    elif resultado_jogo == 'DERROTA':
        lose += 1
    turn += 1
    print('Turn: {} | Vitórias: {} | Derrotas: {}\n'.format(turn, win, lose))

print('Fim do jogo')
if win > lose:
    print('Você venceu!')
elif win == lose:
    print('Empate!')
else:
    print('Você perdeu!')
