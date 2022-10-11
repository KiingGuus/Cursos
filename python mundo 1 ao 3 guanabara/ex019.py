import random
a1=input('Nome do aluno: ')
a2=input('Nome do aluno: ')
a3=input('Nome do aluno: ')
a4=input('Nome do aluno: ')
lista= [a1,a2,a3,a4]
escol= random.choice(lista)
print ('O aluno escolhido é {}'.format(escol))