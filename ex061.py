a = int(input('Digite o primeiro termo da P.A: '))
b = int(input('Digite a razão da P.A: '))
d = a
cont = 1
while cont <= 10:
    print('{} → '.format(d), end='')
    d += b
    cont += 1
print('FIM')
