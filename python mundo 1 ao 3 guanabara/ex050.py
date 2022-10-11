q = 0
s = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        s += +num
        q += 1
print('Existem {} pares entre os numeros. E a soma deles é de {}'.format(q, s))