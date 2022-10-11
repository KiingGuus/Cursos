peso = float(input('Peso: '))
alt = float(input('Altura: '))
imc = peso / alt**2
print('Seu IMC é de {}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade morbida')