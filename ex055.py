maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o {}° peso:'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Maior peso lido foi de {}Kg'.format(maior))
print('Menor peso lido foi de {}Kg'.format(menor))
