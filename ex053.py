'''criar um detector de palíndromo(palavras invertidas nas quais a ordem das letras ficam igual'''

frase = str(input('Digite uma frase: ')).upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase: {}'. format(junto))
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Esta frase é um PALÍNDROMO!')
else:
    print('NÃO é um palíndromo...')

    '''não consegui fazer sozinha'''