p= float(input('Valor do produto R$'))
d= int(input('Digite se o valor é de 5%, 10% ou 15% :'))
if d== 5:
    print('O protudo com 5% de desconto é R${}'.format(p-p*0.05))
elif d== 10:
    print('O protudo com 10% de desconto é R${}'.format(p - p * 0.10))
elif d== 15:
    print('O protudo com 15% de desconto é R${}'.format(p - p * 0.15))