print('-=-' * 40)
print('Informe 3 medidas de seguimento e o computador irá calcular e ver se é possivel forma um triangulo com essas medias!!!')
print('-=-' * 40)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a > b and a > c and a > b + c:
    print('\nNão é possivel fazer um triangulo')
elif b > a and b > c and b > a + c:
    print('\nNão é possivel fazer um triangulo')
elif c > a and c > b and c > a + b:
    print('\nNão é possivel fazer um triangulo')
else:
    print('É possivel fazer um triangulo!!!')
print('-=-' * 40)