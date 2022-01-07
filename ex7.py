s = input('Entre com o sexo M/F: ').upper()
h = float(input('Entre com a altura: '))
peso = 0

if s[0] == 'M':
    peso = (72.7 * h) - 58
    print(peso)
else:
    peso = (62.1 * h) - 44.7
    print(peso)
