primeiro = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('progressão finalizada com {} termos mostrados.'.format(total))
