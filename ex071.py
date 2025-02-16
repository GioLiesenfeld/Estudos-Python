print('=' * 30)
print('{:^30}'.format('Banco CEV'))
print('=' * 30)
valor = int(input('Qual valor deseja sacar? R$'))
tot = valor
ced = 50
totalced = 0
while True:
    if tot >= ced:
        tot -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if tot == 0:
            break
print('=' * 30)
print('Volte sempre ao banco CEV')