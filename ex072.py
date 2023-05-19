x ='Zero', 'Um', 'Dois', 'Três', 'Quatro	', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
cont = ' '
while True:
    num = int(input('Digite um número [0 a 20]:'))
    if num > 20 or num < 0:
        num = int(input('\033[1;31mNúmero inválido, digite novamente [0 a 20]:\033[m'))
    if 0 <= num <= 20:
        print(f'\033[1mVocê digitou {x[num] } !\033[m')
        cont = str(input('Quer continuar [S/N]')) .upper() .strip()
        if cont == 'N':
            break
