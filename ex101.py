def voto(ano):
    from datetime import date
    idade = date.today().year - data
    if idade < 16:
        print('Não vota!')
    elif idade >= 16 and idade <18:
        print('Voto opcional.')
    elif idade >= 18 and idade < 65:
        print('Voto obrigatório!')
    else:
        print('Voto opcional')





data = int(input('Digite o seu ano de nascimento: '))
voto(data)

#fiz sozinha