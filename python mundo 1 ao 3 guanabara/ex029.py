velo= int(input('Velocidade do carro: '))
if velo <= 80:
    print('Dirija com cuidado.')
else:
    print('Você foi multado!!!')
    mult = (velo - 80) * 7
    print('Sua velocidade era de {}km/h e o maximo permitido era de 80km/h. Sua multa é no valor de R${:.2f}'.format(velo, mult))