n1 = float (input('Digite sua primeira nota: '))
n2 = float (input('Digite sua segunda nota: '))
m = (n1 + n2)/2
if m < 5.0:
    print('A sua média: {}\nClassificação: REPROVADO!'.format(m))
elif m > 4.9 and m < 7:
    print('A sua média: {}\nClassificação: RECUPERAÇÃO!'.format(m))
elif m > 6.9 and m <= 10:
    print('A sua média: {}\nClassificação: APROVADO!'.format(m))

    '''maior e menor também pode ser escrito como 6.9 < m <= 10'''