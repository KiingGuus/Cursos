a= input('Digite algo: ')
cores = {'limpa':'\033[m',
         'verm':'\033[31m',
         'verd':'\033[32m'}
print('O tipo primitivo desse valor é {}{}{}.'.format(cores['verd'], type(a), cores['limpa']))
print('Só tem espaços? {}{}{}.'.format('\033[31m', a.isspace(), '\033[m'))
print('É um numero? {}'.format(a.isnumeric()))
print('Esta em minusculo? {}'.format(a.islower()))
print('Esta em maiusculo? {}'.format(a.isupper()))