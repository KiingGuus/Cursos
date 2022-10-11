n1 = float(input('Nota :'))
n2 = float(input('Nota :'))
n3 = float(input('Nota :'))
med = (n1 + n2 + n3) / 3
if med < 5:
    print('Media {:.1f}, Reprovado'.format(med))
elif med < 6.9:
    print('Media {:.1f}, Recuperação'.format(med))
else:
    print('Media {:.1f}, Aprovado'.format(med))