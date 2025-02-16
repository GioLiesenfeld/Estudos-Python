print('-=-' * 20)
print('CADASTRO DE COMPRAS')
print('-=-' * 20)
soma = maiormil = maisb = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).upper().split()
    preco = float(input('Digite o preço: R$ '))
    soma += preco
    maisb = preco
    if preco < maisb:
        barato = nome
    if preco >= 1000:
        maiormil += 1
    resp = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if resp not  in 'SsNn':
        resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=-' * 20)
print('Análise finalizada')
print('-=-' * 20)
print(f'O total da compra foi R${soma}')
print(f'O produto mais barato foi o {barato}') #não consegui por o nome#
print(f'O total de produtos que custam mais de mil reais: {maiormil}')