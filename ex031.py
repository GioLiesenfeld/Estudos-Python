km = float (input('Digite a quilometragem da viagem: '))
if km <= 200:
    v = 0.50 * km
    print('O valor da viagem será R${}'.format(v))
else:
    v = 0.45 * km
    print('O valor da viagem será R${}'. format(v))