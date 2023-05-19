i = int(input('Primeiro termo: '))
p = int(input('Razão: '))

decimo = i + (10 - 1) * p
for c in range(i, decimo + p, p):
    print(c, end=' ➔ ')
print('ACABOU')
