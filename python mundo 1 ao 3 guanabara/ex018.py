import math
ang= float(input('Digite o valor do angulo: '))
cos= math.cos(math.radians(ang))
sen= math.sin(math.radians(ang))
tan= math.tan(math.radians(ang))
print('Angulo: {}\nseno: {:.2f}\ncosseno: {:.2f}\ntangente: {:.2f}'.format(ang, sen, cos, tan))