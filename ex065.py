y = 'S'
cont = valor = maior = menor = 0

while y in 'S':
    x = int(input('Digite um numero: '))
    valor += x
    cont += 1
    if cont == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    y = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = valor/cont
print('Voce digitou {} numeros e a media foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
