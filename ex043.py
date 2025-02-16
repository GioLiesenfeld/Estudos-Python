p = float (input('Digite o seu peso: '))
a = float (input('Digite sua altura: '))
imc = p/(a*a)
if imc < 18.5:
    print('Seu imc: {:.1f}\nVocê está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu imc: {:.1f}\nPESO IDEAL'.format(imc))
elif imc >= 25 and imc < 30:
    print('Sei imc: {:.1f}\nSOBREPESO'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu imc: {:.1f}\nOBESIDADE'.format(imc))
elif imc >= 40:
    print('Seu imc: {:.1f}\nOBESIDADE MÓRBIDA'.format(imc))
elif imc < 0:
        print('POSSIBILIDADE INEXISTENTE')