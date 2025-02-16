num = [[], []]
for c in range(1,8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('=-' * 20)
print(f'Os valores pares digitados: {num[0]}')
print(f'Os valores ímpares digitados: {num[1]}')
#criei uma resolução própria, porém o professor pediu um lista única