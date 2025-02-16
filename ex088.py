jogos = []
lista = []
from time import sleep
from random import randint
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
r = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= r:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
sleep(1)
print('=-' * 20)
print(f'{"SORTEANDO OS JOGOS":^30}')
print('=-' * 20)
sleep(1)
for i, l in enumerate(jogos):
    print(f'O jogo {i+1}: {l}')
    sleep(1)
print('BOA SORTE NO JOGO!')