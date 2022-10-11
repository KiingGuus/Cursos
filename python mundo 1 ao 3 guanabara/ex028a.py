from random import randint
from time import sleep
computador = randint(0, 5)#FAZ O COMPUTADOR PENSAR EM UM NUMERO
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))#JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABENS!!! Você conseguiu vencer!!!')
else:
    print('GANHEI!!! O numero que eu pensei foi {} e não no {}'.format(computador, jogador))