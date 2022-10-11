lar= float(input('Largura da parede: '))
com= float(input('Comprimento da parede: '))
area= lar*com
tin= float(input('Litros de tinta: '))
if tin*2 < area:
    print('Não a tinta o suficiente para pintar a parede.')
else:
    print('Com {}L de tinta voce consegue pintar {}m²'.format(tin,tin*2))