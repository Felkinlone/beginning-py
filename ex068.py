from random import randint
v = 0
while True:
    x = int(input('Diga um valor: '))
    random = randint(0, 11)
    total = x + random
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {x} e o computador {random}. Total de {total}', end='')
    print(' Deu PAR ' if total % 2 == 0 else ' Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Ganhou :D')
            v += 1
        else:
            print('Perdeu :/')
            break
    elif tipo == 'I':
        if x % 2 == 1:
            print('Ganhou :D')
            v += 1
        else:
            print('Perdeu :/')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! voce venceu {v} vezes.')
