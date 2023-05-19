i = int(input('Digite um número: '))
tot = 0
for c in range(1, i + 1):
    if i % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 número {} foi divisível {} vezes'.format(i, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO E PRIMO!')
