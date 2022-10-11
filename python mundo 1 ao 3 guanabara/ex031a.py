dist= float(input('Distancia da viajem: '))
prec= dist * 0.50 if  dist <= 200 else dist * 0.45
print('O preço da passagem sera de {}'.format(prec))