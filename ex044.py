print('{:=^40}'.format('LOJAS LIESENFELD'))
valor = float(input('Digite o valor do produto: R$'))
print('''Digite a forma de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Qual será a forma de pagamento?'))
if opcao == 1:
    desc = valor - ((valor*10)/100)
    print('A opção escolhida: {}\nO valor do produto com 10% de desconto: R${}'.format(opcao,desc))
elif opcao == 2:
    desc = valor - ((valor * 5) / 100)
    print('A opção escolhida: {}\nO valor do produto com 5% de desconto: R${}'.format(opcao, desc))
elif opcao == 3:
    print('A opção escolhida: {}\nO valor total: R${}'.format(opcao,valor))
elif opcao == 4:
    juros = valor + (valor * 20)/100
    print('A opção escolhida: {}\nO valor total com juros (10%): R${}'.format(opcao,juros))