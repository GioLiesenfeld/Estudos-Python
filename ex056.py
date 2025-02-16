médiaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range (1,5):
    nome = str(input('Digite seu nome: ')).strip()
    idade = str(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: F/M ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo == 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'Ff' and idade < 20:
        totmulher20 += totmulher20 + 1

médiaidade = somaidade/ 4
print('A média das idades é: '.format(médiaidade))
print('O homem mais velho possui {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('Há {} mulheres abaixo dos 20 anos.'.format(totmulher20))

'''copiei do vídeo de correção, mas possui algum erro'''