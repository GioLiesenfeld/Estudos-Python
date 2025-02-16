#programa lerá o número digitado pelo usuário(0 a 20) e mostrará o número por extenso)

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
 'dezoito', 'dezenove', 'vinte''')

n = int(input('Digite um número de 0 a 20: '))
while True:
    if  0 <= n <= 20:
        print(f'Você digitou o número {numeros[n]}')
        break
    else:
        n = int(input('Digite outra vez...um número de 0 a 20: '))

