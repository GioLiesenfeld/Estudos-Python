def area(a, b):
    ar = a * b
    print(f'A área do terreno é {ar} m2')


def titulo(texto):
    print('=-'*20)
    print(texto)
    print('=-'*20)

titulo('Controle de Terrenos')
a = float(input('Digite a largura (m): '))
b = float(input('Digite o comprimento (m): '))
area(a, b)

#fiz sozinha