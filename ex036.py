valor = float(input('Valor da casa? R$'))
salario = float(input('Salario do comprador? R$'))
anos = float(input('Quantos anos de financiamento? '))

prestacao = valor/(anos*12)
porcentagem = salario * 30/100

print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f} '.format(valor, anos, prestacao))

if porcentagem >= prestacao:
    print('\033[7mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[0:30:41mEmpréstimo NEGADO!\033[m')
