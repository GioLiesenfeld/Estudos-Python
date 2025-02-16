#aprimorar o desafio 93
dadosj = {}
totg = []
somatotg = 0
jogos = {}
cadastro = {}
while True:
    nome = str(input('O nome do jogador: '))
    cadastro['Nome'] = nome
    qp = int(input('Quantas partidas jogadas? '))
    ngols = []
    for c in range(0,qp):
        gols = int(input(f'Quantos gols na partida {c+1}?'))
        jogos[f'Jogo {c}'] = gols
        totg.append(gols)
        somatotg += gols
    cadastro['Gols'] = totg
    cadastro['Total'] = somatotg
    dadosj = cadastro.copy()
    cadastro.clear()
    r = str(input('Deseja continuar? S/N '))
    if r in 'Nn':
        break
print('=-'*20)
for c, v in dadosj.items():
    print(f'{c} corresponde a {v}')
print('=-' *20)
print(dadosj)
for p in dadosj.items():
    print(f'{nome} {totg} {somatotg}')
print('=-' *20)
print(f'O total de gols foi {somatotg}')
print(cadastro)
print(dadosj)