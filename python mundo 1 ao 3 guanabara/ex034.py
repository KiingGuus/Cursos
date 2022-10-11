sala = float(input('Digite o valor do seu salario: '))
if sala > 1250:
    print('Seu salario com 10% de aumento é de R${:.2f}'.format(sala * 0.1 + sala))
else:
    print('Seu salario com 15% de aumento é de R${:.2f}'.format(sala * 0.15 + sala))