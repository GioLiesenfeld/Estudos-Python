resp = 'S'
media = quant = soma = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if menor < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = soma/quant
print('ACABOU')
print('A soma dos números é: {}'.format(soma))
print('A quantidade de números digitados foi: {}'.format(quant))
print('A média de números digitados é: {:.2f}'.format(media))
print('O maior número é {} e o menor é {}'.format(maior, menor))