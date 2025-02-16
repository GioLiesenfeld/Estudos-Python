from time import sleep
print('='*20)
print('OPÇÕES DE OPERAÇÕES')
print('='*20)
print(' ')
op = ' '
produto = 0
while op != 5:
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    op = int(input('''Digite a opção de operação desejada:
    [1] Somar
    [2] Multiplicar
    [3] Maior       
    [4] Novos números
    [5] Sair da operação '''))
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é: {}'.format(n1, n2, soma))
    elif op == 2:
            produto = (n1 * n2)
            print('A multiplicação entre {} e {} é: {}'.format(n1, n2, produto))
    elif op == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
            print('O maior número é o {}'.format(maior))
        elif n1 == n2:
            print('Os números são iguas!')
    elif op == 3:
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif op == 5:
        print('Finalizando...')
        sleep(1)


