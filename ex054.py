from datetime import date
np = 0
for c in range (1,8):
    ano = int(input('Digite o ano de seu nascimento: '))
    idade = date.today().year - ano
    if idade < 18:
        print('Sua idade: {} anos'.format(idade))
        print('Você ainda não completou a maioridade!')
    if idade >= 18:
        np = np + 1
        print('Sua idade: {} anos'.format(idade))
        print('Você já completou a maioridade!')
print('O número de pessoas maiores de idade são: {}'.format(np))

'''Não consegui colocar o número de pessoas maiores de idade = = consegui depois, fiz sozinha'''