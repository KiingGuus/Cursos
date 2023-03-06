print('===='*10)
print('10 termos de uma pa'.upper())
print('===='*10)


primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(1 , 11, 1):
    print('{}'.format(primeiroTermo), end=' -> ')
    primeiroTermo += razao
print('ACABOU!')