#criar um programa que leia os 20 primeiros colocados na tabela do brasileirao

tabela = ('Flamengo', 'Palmeiras', 'Bahia', 'Botafogo', 'Atlético-PR', 'Bragantino', 'Internacional',
'Cruzeiro', 'Cruzeiro', 'São Paulo', 'Atlético-MG', 'Fortaleza', 'Juventude', 'Criciúma', 'Cuiabá',
'Vasco da Gama', 'Atlético-GO', 'EC vitória', 'Corinthians', 'Grêmio', 'Fluminense')

print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os últimos 4 colocados são: {tabela[-4:]}')
print('')
print(sorted(tabela))
print('')
print(f'O time Grêmio se encontra na posição {tabela.index('Grêmio')}') #sozinha