#criar uma lista com números digitados pelo usuário, no final mostrar a lista filtrada entre números pares, ímpares e
#total de números

numeros = []
impares = []
pares = []
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Deseja continuar? S/N '))
    if r in 'Nn':
        break
print('=-' * 30)
print(f'Os números digitados foram: {numeros}')
print(f'Os números pares digitados: {pares}')
print(f'Os números ímpares digitados: {impares}')

#fiz totalmente sozinha