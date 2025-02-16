c = quant = n = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    quant += n
    c += 1
print('FIM')
print('-' * 20)
print(f'A soma dos valores digitados é: {quant}')
print(f'O número de valores digitados é: {c}')
