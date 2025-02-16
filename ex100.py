from random import randint
def sorteia(lista):
    for c in range(0,5):
        lista.append(randint(1, 10))

def somaPar(pares):
    soma = 0
    for c in pares:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares é de {soma}')

numeros = list()
sorteia(numeros)
print(numeros)
somaPar(numeros)

#consegui sozinha