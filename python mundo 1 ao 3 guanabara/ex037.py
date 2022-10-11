co = {'lim': '\033[m',
      'verm': '\033[31m',
      'verd': '\033[32m',
      'ama': '\033[33m',
      'az': '\033[34m',
      'rox': '\033[35m',
      'azb': '\033[36m',
      'cin': '\033[37m',}
n = int(input('Digite um numero: '))
print('''Escolha uma das opões:
[1] para BINARIO
[2] para OCTAL
[3] para HEXADECIMAL''')
opc = int(input('Digite sua escolha: '))
if opc == 1:
    print('O numero {}{}{} em BINARIO é {}{}{}'.format(co['ama'], n, co['lim'], co['verd'], bin(n)[2:], co['lim']))
elif opc == 2:
    print('O numero {}{}{} em OCTAL é {}{}{}'.format(co['ama'], n, co['lim'], co['verd'], oct(n)[2:], co['lim']))
elif opc == 3:
    print('O numero {}{}{} em HEXADECIMAL é {}{}{}'.format(co['ama'], n, co['lim'], co['verd'], hex(n)[2:], co['lim']))
else:
    print('{}OPÇÃO NÃO VALIDA!!!{}'.format(co['verm'], co['lim']))