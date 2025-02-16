from random import randint
from time import sleep
palpites = 1
computador = randint(0,5) #faz o pc sortear
print('--=--' * 20)
print('Vou pensar em um número entre 0 e 5...tente adivinhar...')
print('--=--' * 20)
jogador = int (input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
while jogador != computador:
    jogador = int(input('Ops..PC = {} X JOGADOR = {}. Tente outra vez!'.format(computador,jogador)))
    palpites = palpites + 1
    if jogador == computador:
        print('Você ADIVINHOU! O número oculto era o {} '.format(jogador))
        print('Para vencer, foram necessários {} palpites.'.format(palpites))