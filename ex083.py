'''exp = str(input('Digite sua expressão: '))
cont = 0
for sim in exp:
    if sim == '(':
        cont += 1
    elif sim == ')':
        cont += 1
if cont % 2 == 0:
    print('Expressão válida!')
else:
    print('Expressão NÃO válida!')'''

exp = str(input('Digite a expressão: '))
pilha = []
for sim in exp:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é VÁLIDA!')
else:
    print('Sua espressão está ERRADA!')