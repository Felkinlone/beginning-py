from datetime import date

mouf = str(input('Você e HOMEM(h) ou MULHER(m)? '))

if mouf == 'm':
        print('Você não precisa fazer o alistamento militar!')

elif mouf == 'h':
    data = int(input('Ano de nascimento: '))
    idade  = date.today().year - data


    if idade == 18:
        print('Quem nasceu em {} tem {} anos em {}.'.format(data, idade, date.today().year))
        print('Você tem que se alistar IMEDIATAMENT!')
    elif idade > 18:
        print('Quem nasceu em {} tem {} anos em {}.'.format(data, idade, date.today().year))
        print('Você deveria ter se alistado há {} anos'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(date.today().year - (idade-18)))
    elif idade - data < 18:
        print('Quem nasceu em {} tem {} anos em {}.'.format(data, idade, date.today().year))
        print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
        print('Seu alistamento sera em {}.'.format( date.today().year - (idade - 18)))
