#criar uma lista com números digitados pelo usuário,
valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado...não será adicionado novamente.')
    r = str(input('Deseja continuar? S/N '))
    if r in 'Nn':
        break
print('=-' * 30)
print(f'Os números digitados foram: {valores}')
valores.sort()
print(f'A sua ordem crescente: {valores}')