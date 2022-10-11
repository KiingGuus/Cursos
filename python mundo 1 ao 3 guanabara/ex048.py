soma = 0
count = 0
for c in range(3, 500, 3):
    if c % 2 != 0:
        soma += c
        count += 1
print('Existem {} numeros impares multilos de tres entre 1 e 500. E a soma de tolodos eles é de {}'.format(count, soma))
