x = int(input('Qual o salario do funcionario? R$'))
if x <= 1250:
    novo = x + ( x * 15/100)
else:
    novo = x + (x * 10/100)
print('Quem ganhava {} passa a ganhar R${:.2f} agora'.format(x, novo))
