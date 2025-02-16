from datetime import date
cadastro = {}
a = date.today().year
while True:
    cadastro['Nome'] = str(input('Digite seu nome: '))
    ano = int(input('Ano de nascimento: '))
    idade = (a - ano)
    cadastro['Idade'] = idade
    ncart = int(input('Número da carteira de trabalho (0 NÃO TEM): '))
    if ncart == 0:
        cadastro['Nº CTPS'] = ncart
        break
    cadastro['Nº CTPS'] = ncart
    anoc = int(input('Ano de contratação: '))
    cadastro['Ano de contratação'] = anoc
    sal = float(input('Salário: '))
    cadastro['Salário'] = sal
    sub = a - anoc
    apos = 35 - sub
    cadastro['Aposentadoria'] = apos
    break
print('=-' * 15)
print(f'{"DADOS CADASTRAIS":^30}')
print('=-' * 15)
for p, c in cadastro.items():
    print(f'{p} corresponde a {c}')
#orgulho define