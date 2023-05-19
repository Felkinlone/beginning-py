from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opt = 0
while opt != 5:
    print('''             [ 1 ] Somar
             [ 2 ] Multiplicar
             [ 3 ] Maior
             [ 4 ] Novos Números
             [ 5 ] Sair do Programa''')
    opt = int(input('>>>>>>>>> Digite sua opção: '))
    if opt == 1:
        soma = n1+n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
        print(20*'=-')
    elif opt == 2:
        multi = n1 * n2
        print(('A multiplicação entre {} e {} é {}'.format(n1, n2, multi)))
        print(20*'=-')
    elif opt == 3:
        if n2 < n1:
            maior = n1
            print('entre {} e {}, o maior é {}'.format(n1, n2, maior))
            print(20 * '=-')
        elif n2 > n1:
            maior = n2
            print('entre {} e {}, o maior é {}'.format(n1, n2, maior))
            print(20 * '=-')
        else:
            print('Os dois números, {} e {}, são iguais'.format(n1, n2))
            print(20 * '=-')
    elif opt == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opt == 5:
        print('finalizando')
        print('...')
        sleep(2)
        print('fim do programa! volte sempre!')
    else:
        print('opção inválida')
