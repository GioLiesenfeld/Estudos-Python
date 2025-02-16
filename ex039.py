from datetime import date
atual = date.today().year
print('--=--'*20)
print('ANÁLISE DE ALISTAMENTO')
print('--=--'*20)
print('Ano atual: {}'.format(atual))
sexo = str(input('Digite seu sexo (feminino/masculino):')). upper()
if sexo == 'FEMININO':
    print("Você não precisa de alistamento")
elif sexo == 'MASCULINO':
    a = int(input('Digite seu ano de nascimento: '))
    id = atual - a
    if id < 18:
        t = 18 - id
        print('Você deverá se alistar no FUTURO!\nFaltam {} anos para se alistar. '.format(t))
        print('Sua idade a ser completada em {} é {} anos.'.format(atual, id))
    elif id == 18:
        print('Você deve se ALISTAR!')
        print('Sua idade a ser completada em {} é {} anos.'.format(atual, id))
    elif id > 18:
        t = id - 18
        print('Seu processo de alistamento já deve ter sido CONCLUÍDO.\nSe passaram {} anos.'.format(t))
        print('Sua idade a ser completada em {} é {} anos.'.format(atual, id))