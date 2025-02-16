#olhar o vídeo de resolução e fazer junto
from time import sleep

def maior (* num):
    cont = maior = 0
    print('=-' * 20)
    print('\nAnalisando números...')
    for v in num:
        print(f'{v}', end= ' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram digitados {cont} valores.')
    print(f'O maior valor é {maior}')




#Programa principal
maior(2, 9, 4, 5, 7, 1)