cadastrados = []
processo = {}
quantp = 0
id = 0
mulheres = []
pessoasmi = []
medid = 0
while True:
    nome = str(input('Nome: '))
    quantp += 1
    idade = int(input('Idade: '))
    id += idade
    sexo = str(input('Sexo: M/F '))
    if sexo in 'Ff':
        mulheres.append(nome)
    processo['Nome'] = nome
    processo['Idade'] = idade
    processo['Sexo'] = sexo
    cadastrados.append(processo.copy())
    r = str(input('Deseja continuar? S/N '))
    if r in 'Nn':
        break
for p in cadastrados:
    if idade > medid:
        pessoasmi = nome
medid = id/quantp
print(processo)
print(cadastrados)
print(id)
print(medid)
print('=-'*30)
print(f'O total de pessoas cadastradas é de {quantp}')
print(f'A média de idade de um grupo é de {medid} anos')
print(f'As mulheres cadastradas: {mulheres}')
print(f'As pessoas com idade acima da média são: {pessoasmi}')
