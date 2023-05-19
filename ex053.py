frase = str(input('Digite o palíndromo:  ')).strip().upper()
x = frase.split()
junto = ''.join(x)
inverso = junto[::-1]

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não e um palíndromo')
