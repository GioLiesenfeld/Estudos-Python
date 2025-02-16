listagem = ('pão', 1, 'alface', 3, 'suco', 3.50, 'caderno', 5.0, 'marca texto', 10.0)
print('-' * 30)
print(f'{"LISTA DE COMPRAS":^20}')
print('-' * 30)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-'*30)