dist= float(input('Distancia da viajem: '))
if dist<= 200:
    print('Ira pagar R$0,50 pra cada km. O valor da viajem é de {:.2f}'.format(dist*0.50))
else:
    print('Ira pagar R$0,45 pra cada km. O valor da viajem e de {:.2f}'.format(dist*0.45))