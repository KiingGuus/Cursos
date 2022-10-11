km= float(input('Km rodados: '))
da= int(input('Dias alugados: '))
kmr= da*0.15
dar= da*60
print('Voce alugou o carro por {} dias e percorreu um total de {}km. o valor do aluguel do é de R${}'.format(da,km,kmr+dar))