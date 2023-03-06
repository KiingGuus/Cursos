num = int(input('Digite um numero: '))
primo = 0
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end= '')
        cont += 1
    else:
        print('\033[m', end= '')
    print('{} '.format(c), end='')
print('\nO numero {} foi divivisel {} vezes.'.format(num, cont))
if cont == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele nao é primo.')