n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 < n2 and n1 < n3:
    menor = n1
    print ('O menor número é: {}'. format(menor))
if n2 < n3 and n2 < n1:
    menor = n2
    print('O menor número é: {}'.format(menor))
if n3 < n1 and n3 < n2:
    menor = n3
    print('O menor número é: {}'.format(menor))
