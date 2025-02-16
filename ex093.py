dadosj = {}
totg = []
somatotg = 0
jogos = {}
nome = str(input('O nome do jogador: '))
dadosj['Nome'] = nome
qp = int(input('Quantas partidas jogadas? '))
ngols = []
for c in range(0,qp):
    gols = int(input(f'Quantos gols na partida {c+1}?'))
    jogos[f'Jogo {c}'] = gols
    totg.append(gols)
    somatotg += gols
dadosj['Gols'] = totg
dadosj['Total'] = somatotg
print('=-'*20)
print(dadosj)
print('=-'*20)
for c, v in dadosj.items():
    print(f'{c} corresponde a {v}')
print('=-' *20)
for c, v in jogos.items():
    print(f'No {c} marcou {v} gols')
print('=-' *20)
print(f'O total de gols foi {somatotg}')