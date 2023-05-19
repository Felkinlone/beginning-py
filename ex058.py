from random import randint
from time import sleep

chose = 'Y'
print('{:^55}'.format('\033[0:30:41m JOKENPÔ DO BRUNÃO \033[m'))
print('[ 1 ] PEDRA - [ 2 ] PAPEL - [ 3 ] TESOURA')

while chose not in 'Nn':
    print('{:^40}'.format('Faça sua escolha'))
    x = int(input())
    print('JO...')
    sleep(0.5)
    print('KEN...')
    sleep(0.5)
    print('PO...')
    sleep(0.5)

    computador = (randint(1, 3))
    if computador == 1:
        if ( x == 1):
            print('✊ vs ✊ \033[7:37:40mEMPATE\033[m!!')
        elif (x == 2):
            print('✊ vs ✋ \033[0:30:41mVôCE GANHOU SEU PUTO!!!\033[m')
        elif (x == 3):
            print('✊ vs ✌ \033[0:30:46mTENTOU, MAS ELE É SUPERIOR\033[m')
        else:
            print('Numero digitado invalido')
    elif computador == 2:
        if ( x == 1):
            print('✋ vs ✊ \033[0:30:46mTENTOU, MAS ELE É SUPERIOR\033[m')
        elif (x == 2):
            print('✋ vs ✋ \033[7:37:40mEMPATE!!\033[m')
        elif (x == 3):
            print('✋ vs ✌ \033[0:30:41mVôCE GANHOU SEU PUTO!!!\033[m')
        else:
            print('Numero digitado invalido')
    else:
        if ( x == 1):
            print('✌  vs ✊ \033[0:30:41mVôCE GANHOU SEU PUTO!!!\033[m')
        elif (x == 2):
            print('✌  vs ✋ \033[0:30:46mTENTOU, MAS ELE É SUPERIOR\033[m')
        elif (x == 3):
            print('✌  vs ✌ \033[7:37:40mEMPATE!!\033[m')
        else:
            print('Numero digitado invalido')
    chose = str(input('Jogar novamente? [Y/N]'))
