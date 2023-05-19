while True:
    x = int(input('Quer ver a tabuada de qual valor? '))
    if x < 0:
        break
    print(6 * '~~')
    for c in range(1, 11):
        print(f'{x} X {c} = {c * x}')
    print(6 * '~~')
print('Obrigado por usar!')
