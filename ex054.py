from datetime import date
tot = 0
for c in range(0, 7):
    x = int(input('Em que ano a {} pessoa nasceu? '.format(c+1)))
    idade = date.today().year - x
    if idade >= 21:
        tot += 1
    y = 7 - tot
print('{} Pessoas são maiores de idade'.format(tot))
print('{} Pessoas são menores de idade'.format(y))
