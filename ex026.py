x = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(x.count('A')))
print('A primeira letra A apareceu na posição {}'.format(x.find('A')+1))
print('A última letra A apareceu na posição {}'.format(x.rfind('A')+1))