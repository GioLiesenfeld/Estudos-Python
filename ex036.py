valorcasa = float ( input('Digite o valor da casa: '))
sal = float (input('Digite seu salário: '))
anos = int (input('Em quanto tempo deseja pagar(número de anos): '))
vpa = valorcasa/anos
parcela = vpa/12
psal = (sal * 30)/ 100
print (psal)
print('O valor da casa: R${}'.format(valorcasa))
print('Seu salário: R${}'.format(sal))
print('Quantos anos de pagamento: {}'.format(anos))
print('O valor da parcela: R${}'.format(parcela))
if parcela <= psal:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')