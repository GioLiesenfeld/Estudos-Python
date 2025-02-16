nome=str(input('Digite seu nome completo: ')).strip()
print('ANÁLISE')
print()
print('Nome digitado: {}'.format(nome))
print('O nome em maiúsculo: {}'.format(nome.upper()))
print('O nome em letras minúsculas: {}'. format(nome.lower()))
print('O número de letras é: {}'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#exercício realizado com auxílio do vídeo de resolução.