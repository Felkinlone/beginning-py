n = str(input('[M/F]')).strip().upper()[0]
while n not in 'MmFf':
    n = str(input('Digite um genero valido [M/F]')).strip().upper()[0]
if n in 'Mn':
    print('Masculino')
else:
    print('Feminino')
