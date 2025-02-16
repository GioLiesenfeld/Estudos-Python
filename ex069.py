print('-=-' * 20)
print('CADASTRO DE PESSOAS')
print('-=-' * 20)
print('--' * 20)
homens = maioridade = fmenor = 0
while True:
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        maioridade += 1
    sexo = str(input('Digite seu sexo [F/M]: ')).upper().split()[0]
    if sexo not in 'FfMm':#                                          '''usar !=, == para números'''
        sexo = str(input('Digite seu sexo [F/M] ')).upper().split()[0]
    if sexo in 'Mm':
        homens += 1
    if idade < 18 and sexo in 'Ff':
        fmenor += 1
    resp = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if resp in 'Nn':
        break
print('ACABOU!')
print('-=-' * 20)
print('FIM DE CADASTRO')
print('-=-' * 20)
print(f'O total de homens cadastrados: {homens}')
print(f'O total de pessoas maiores de idade: {maioridade}')
print(f'O total de mulheres menores de idade é: {fmenor}')

