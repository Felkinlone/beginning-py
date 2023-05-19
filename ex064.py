cont = nun = soma = 0

nun = int(input('Digite um número  [999 para parar]: '))
while nun != 999:
    soma += nun
    cont += 1
    nun = int(input('Digite um número  [999 para parar]: '))

print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))
