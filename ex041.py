from datetime import date
print('CLASSIFICAÇÃO DOS NADADORES')
print('='* 20)
ano = int(input('Digite o ano de seu nascimento: '))
anoa = date.today().year
id =  anoa - ano
if id <= 9:
    print('CATEGORIA MIRIM')
elif id > 9 and id <= 14:
    print('CATEGORIA INFANTIL')
elif id > 14 and id <= 19:
    print('CATEGORIA JÚNIOR')
elif id > 19 and id <= 20:
    print('CATEGORIA SÊNIOR')
elif id > 20:
    print('CATEGORIA MASTER')

    '''TAMBÉM: id <= 9...
               id <= 14
               id <= 19
               id <= 25
else: ...'''