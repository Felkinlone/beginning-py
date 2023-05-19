distancia = float(input('Qual é a distancia da sua viagem? '))
print('Voce está prestes a começar uma viagem de {}Km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço  da sua passagem sera de R${:.2f}'.format(preco))