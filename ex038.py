n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    maior = n1
    print('O MAIOR número é o {}!'.format(maior))
elif n2 > n1:
    maior = n2
    print('O MAIOR número é o {}!'.format(maior))
elif n1 == n2:
    print('Os números possuem o mesmo valor que é: {}'.format(n1))
