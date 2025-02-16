#criar uma lista com números informados e apresentar o maior valor em sua posição e o menor valor em sua posição

#valores = list()
#for c in range(0,5):
    #valores.append(int(input('Digite um valor: ')))
#print(f'Os valores digitados são {valores}')

#print(f'O maior valor digitado é o {max(valores)} e se encontra nas posição {valores.index(max(valores))}', end= ' ')
#print(f'O menor valor digitado é o {min(valores)} e se encontra nas posição {valores.index(min(valores))}', end= ' ')
#for c, v in enumerate(valores):

#fiz sozinha em 10 min

listanum = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input('Digite um número: ')))
#print(listanum)
    if c == 0:
        mai = men = listanum[0]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Voce digitou os números: {listanum}')
print(f'O maior número é o {mai} que aparece nas posições: ', end=' ')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end=' ')
print()
print(f'O menor número é o {men} que aparece nas posições: ', end=' ')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end=' ')
#não consegui sozinha