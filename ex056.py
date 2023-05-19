somaidade = 0
maioridade = 0
media = 0
nomevelho = 0
muie20 = 0
for c in range(1, 5):
    print(5*'=', '{}° PESSOA'.format(c), 5*'=')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        muie20 += 1
media = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(muie20))
