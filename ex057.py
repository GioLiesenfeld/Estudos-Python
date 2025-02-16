sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite seu sexo: '))
print('Sexo {} registrado com sucesso!'.format(sexo))


'''Não consegui fazer o exercício sozinha'''