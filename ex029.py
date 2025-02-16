from time import sleep
v = float(input('Digite a velocidade do veículo: '))
if v <= 80:
    print('Você está dentro do limite de velocidade!PARABÉNS!')
else:
    print('Você ultrapassou o limite de velocidade.')
    m = (v-80) * 7
    print('CALCULANDO MULTA...')
    sleep(2)
    print('A sua multa foi de R${}'.format(m))