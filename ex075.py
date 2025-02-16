num = (int(input('Digite um número: ')), int(input('Digite um segundo número: ')),
       int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(' ')
print(f'Os números digitados foram {num}.')
print(f'O números 9 aparece {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 aparece na posicão {num.count(3)+1}')
else:
    print('O valor 3 não aparece nesta tupla.')
print('Os valores pares digitados foram ', end= '')
for n in num:
    if n % 2 == 0:
        print (n, end=', ')