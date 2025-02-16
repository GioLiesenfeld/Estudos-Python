D=float(input('Digite a quantidade de dias com o carro: '))
km=float(input('Digite a quilometragem percorrida no período: '))
qd=D*60
qkm=km*0.15
tot=qd+qkm
print('===GASTOS TOTAIS===')
print('A quantidade de dias: {}\nA quilometragem: {}Km\nO total a pagar: R${}'.format(D,km,tot))