#fazer assistindo a aula
"""
->Calcula o fatorial de um número
param n: número a ser calculado
param show: (opcional) mostrar ou não o cálculo
param return: valor do cálculo
"""
def fatorial (n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} ', end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f


print(fatorial(5, show=True))
#help(fatorial)

#fiz assistindo