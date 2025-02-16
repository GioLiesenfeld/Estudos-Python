matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = scol = mai = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('Digite um número: '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
print('-=' * 20)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end= ' ')
    print()
for l in range(0,3):
    scol += matriz[l][2]
for l in range(0,3):
    if mai == 0:
        mai = matriz[1][c]
    if matriz[l][1] > mai:
        mai = matriz[l][1]
print('-=' * 20)
print(f'A soma de todos os números pares é: {spar}')
print(f'A soma da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é: {mai}')
#comecei assistindo a resolução, mas terminei sozinha