from math import hypot
o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
x = hypot(o, a)
print('A hipotenusa vai medir {:.2f}' .format(x))