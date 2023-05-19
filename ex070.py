soma = mil = menor = cont = 1
barato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()[0]
    preço = float(input('Digite o valor do produto: R$'))
    cont += 1
    soma += preço
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Fim do programa')
print(f'Total gasto na compra: R${soma:.2f}')
print(f'{mil} Produtos com valor acima de R$1.000')
print(f'O produto mais barato é {barato} que custa R${menor:.2f}')
