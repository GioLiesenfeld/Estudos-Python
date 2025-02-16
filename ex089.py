ind = []
boletim = []
cadastro = []
media = []
m = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2)/2
    media.append(nome)
    media.append(m)
    cadastro.append(nome)
    cadastro.append(n1)
    cadastro.append(n2)
    ind.append(cadastro[:])
    cadastro.clear()
    boletim.append(media[:])
    media.clear()
    r = str(input('Deseja continuar? S/N '))
    if r in 'Nn':
        break
print(ind)
print(boletim)
print('-=' * 20)
print(f'{"ENTREGA DE BOLETINS":^10}')
print(f'=-' * 20)
print(f'{"Nº":<4} | {"NOME":<8}            | {"MÉDIA":>8}')
for c, v in enumerate(boletim):
    print(f'{"c"}, {["v[0]"]}, {["v[1]"]}')
while True:
    consulta = int(input('Deseja consultar as notas de algum aluno? (999 interrompe) '))
#não copiei da aula, porém não terminei