print('{:=^40}'.format('Lojas da Paulinha'))
compra = float(input('Preço das compras: R$'))

print(6*'==')
print('Formas de pagamento'
      '\n[ 1 ] à vista dinheiro/pix'
      '\n[ 2 ] à vista cartão'
      '\n[ 3 ] 2x no cartão'
      '\n[ 4 ] 3x ou mais no cartão')
print(6*'==')

opcao = int(input('Qual é a opção? '))
if opcao == 1:
      print('Vc vai pagar {:.2f} com 10% de desconto incluido'.format(compra - (compra * 10 / 100)))
elif opcao == 2:
      print('Vc vai pagar {:.2f} com 5% de desconto incluido'.format(compra - (compra * 5 / 100)))
elif opcao == 3:
      print('Vc vai pagar {:.2f} sem descontos'.format(compra))
elif opcao == 4:
      nparcelas = int(input('Quantas parcelas? '))
      parcelas = compra / nparcelas
      valor = parcelas + (parcelas * 20/100)
      print('Sua compra será parcelada em {} vezes de R${:.2f} COM JUROS'.format(nparcelas, valor))
      print('Vc vai pagar {:.2f} com 20% de juros'.format(nparcelas * valor))
else:
      print('Opção invalida de pagamento, tente novamente!')
