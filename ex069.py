maior = homens = mulheres = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
