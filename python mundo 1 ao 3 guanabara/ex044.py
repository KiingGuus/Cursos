pre = float(input('Preço: '))
opc = int(input('''Escolha a opção que deseja:
[1] à vista dinheiro/cheque: 10% de desconto
[2]  à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros
:'''))
if opc == 1:
    print('''Valor: R${}
Desconto de 10% equivale a R${}
O valor da compra é de R${}'''.format(pre, pre * 0.10, (pre * 0.10 - pre) * -1))
elif opc == 2:
    print('''Valor: R${}
Desconto de 5% equivale a R${}
O valor da compra é de R${}'''.format(pre, pre * 0.05, (pre * 0.05 - pre) * -1))
elif opc == 3:
    print('''Valor: R${}
Duas parcelas de R${:.2f}'''.format(pre, pre / 2))
elif opc == 4:
    print('''Valor: R${}  +  20% de JUROS
Valor do JUROS R${}
Tres parcelas de R${:.2f}'''.format(pre, pre * 0.20, (pre * 0.20 + pre) / 3))