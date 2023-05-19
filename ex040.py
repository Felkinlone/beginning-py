n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a primeira nota: '))

m = (n1+n2)/3
if m < 5:
    print('Reprovado')
elif 7 > m >= 5:
    print('Recuperação')
else:
    print('Aprovado')
