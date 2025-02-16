'''ler 6 número e somar os pares'''
par = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par = par + n
        cont = cont + 1
print('A soma dos {} números PARES digitados é: {}'.format(cont, par))

'''não tinha conseguido por os acumuladores e contadores'''
