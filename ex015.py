dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total = dias*60 + 0.15*km
print('O total a pagar é de: R${:.2f}'.format(total))
