sal = float(input('Digite seu atual salário: '))
if sal <= 1250:
    nsal = sal + ((15 * sal)/100)
    print('Seu salário é: R${} \nSeu salário passará a ser: R${}'.format(sal,nsal))
else:
    nsal = sal + ((10 * sal)/100)
    print('Seu salário é: R${} \nSeu salário passará a ser: R${}'.format(sal, nsal))