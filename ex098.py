from time import sleep

def titulo(texto):
    print('~' * len(texto))
    print(texto)
    print('~' * len(texto))

titulo('CONTAGEM')
sleep(0.5)
print('Contagem até 10!')
for c in range(1, 11, 1):
    print(f'{c}', end= ' ')
    sleep(0.5)
sleep(1)
print()
print('Contagem regressiva!')
for c in range(10, 1, -1):
    print(f'{c}', end=' ')
    sleep(0.5)

def contador(a, b, p):

    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end= ' ')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end= ' ')
            sleep(0.5)
            cont -= p
        print('FIM')
    for c in range(a, b, p):
        print(c, end=' ')
    print(' ')
print('FIM')



titulo('Agora vamos personalizar a contagem!')
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
p = int(input('Deseja contar de quanto em quanto? '))
contador(a, b, p)

#não consegui fazer a contagem regressiva