r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Os segmento NÃO podem formatar triangulo')
elif r1 == r2 == r3:
        print('Triangulo equilatero')
elif r1 != r2 != r3 != r1:
        print('Triangulo escaleno')
else:
        print('Triangulo isosceles')
