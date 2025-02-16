coleta = []
dados = []
mai = men = 0
while True:
    coleta.append(str(input('Nome: ')))
    coleta.append(float(input('Peso: ')))
    if len(dados) == 0:
        mai = men = coleta[1]
    else:
        if coleta[1] > mai:
            mai = coleta[1]
        if coleta[1] < men:
            men = coleta[1]
    dados.append(coleta[:])
    coleta.clear()
    r = str(input('Deseja continuar? S/N '))
    if r in 'Nn': break
print('=-' * 20)
print(f'O toltal de pessoas cadastradas foi de {len(dados)} pessoas.')
print(f'O maior peso foi de {mai}. Peso de ', end= ' ')
for p in dados:
    if p[1] == mai:
        print(f'[{p[0]}]', end= ' ')
print(f'O menor peso foi de {men}. Peso de ', end= ' ')
for p in dados:
    if p[1] == men:
        print(f'[{p[0]}]', end= ' ')
#precisei assistir a aula e anotar as ideias do professor