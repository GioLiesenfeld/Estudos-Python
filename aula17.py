num = [1, 2, 3, 4, 5]
print(num)
print(num[0])
print(num[-1])
num.append(6)
print(num)
del num[2]
print(num)
num.pop(4)
print(num)
valores = list(range(4,11))
print(valores)
valores.sort(reverse=True)
print(valores)
print(len(valores))
valores.insert(2, 9)
print(valores)
if 9 in valores:
    valores.remove(9)
else:
    print('Não achei o 9!')
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista!')

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')