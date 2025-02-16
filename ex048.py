'''calcular todos os números ímpares e múltiplos de 3 entre 1 e 500 '''
soma = 0
cont = 0
for c in range (1, 500, 2):
    if c % 3 == 0:
        print(c)
        soma = soma + c
        cont = cont + 1
print('A soma de todos os valores solicitados é: {}'.format(soma))
print('O total de valores solicitados é: {}'.format(cont))