from random import randint
jogos = {}
ordem = []
mai = men = 0
for c in range(1,5):
    jogos[f'Jogador {c}'] = randint(1,7)
print('=-' * 20)
print('SORTEIO DOS JOGADORES')
print('---'* 10)
n = 1
for j, n in jogos.items():
    print(f'{j} sorteou o {n}')
print('-=' * 20)
for c, v in jogos.items():
    print(f' {c}º lugar o {j} com {v}')
print(c)
