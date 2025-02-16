import random
from time import sleep
from random import randint
lista = ('Pedra','Papel','Tesoura')
pc = randint (0, 2)
print('='*20)
print('PEDRA, PAPEL E TESOURA')
print('='*20)
print('''OPÇÕES DE ESCOLHA
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')
jogador = int(input('Digite sua escolha: '))
print('='*20)
sleep(1)
print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura!!!')
sleep(1)
print('O computador jogou: {}'.format(lista[pc]))
print('O jogador jogou: {}'.format(lista[jogador]))
print('='*20)
if pc == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('O você VENCEU!')
        print('O papel embrulhou a pedra!')
    elif jogador == 2:
        print('O computador venceu!')
        print('A pedra quebrou a tesoura!')
elif pc == 1:
    if jogador == 0:
        print('O computador venceu!')
        print('O papel embrulhou a pedra!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('O computador venceu!')
        print('O papel corta a tesoura.')
elif pc == 2:
    if jogador == 0:
        print('O jogador venceu!')
        print('A pedra quebra a tesoura.')
    elif jogador == 1:
        print('O computador venceu!')
        print('A tesoura corta o papel.')
    elif jogador == 2:
        print('Empate!')
else:
    print('OPÇÃO INVÁLIDA!')