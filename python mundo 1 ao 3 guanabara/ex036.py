from time import sleep
cores = {'limp':'\033[m',
         'verme':'\033[31m',
         'verde':'\033[32m',
         'amar':'\033[33m'}
print('\033[33m-=\033[m' * 33)
print('\033[33m-=\033[m' * 33)
vc = float(input('Digite o valor da casa R$'))
sa = float(input('Seu salario R$'))
pre = int(input('Prestações: '))
a = sa * 0.30
b = vc / pre
print('\033[33m-=\033[m' * 33)
sleep(1)
print('PROCESSANDO')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
if pre > 50:
    print('Não é permitido um parcelamento acima de 50X')
    print('{}NEGADO{}'.format(cores['verme'], cores['limp']))
elif b > a:
    print('O valor do parcelamento não pode execeder {}30%{} do salario do comprador.'.format(cores['amar'], cores['limp']))
    print('{}NEGADO{}'.format(cores['verme'], cores['limp']))
else:
    print('{}PARCELAMENTO AUTORIZADO!!!{}'.format(cores['verde'], cores['limp']))
    print('O valor do parcelamento sera de {}{}{} com um total de {}{}{} parcelas'.format(cores['verde'], b,cores['limp'],cores['verde'], pre, cores['limp']))