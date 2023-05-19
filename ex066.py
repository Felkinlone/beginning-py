soma = cont = 0
while True:
    nun = int(input('Digite um número  [999 para parar]: '))
    if nun == 999:
        break
    soma += nun
    cont += 1
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}')
