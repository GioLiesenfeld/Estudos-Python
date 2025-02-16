#criar um programa que leie vários números e coloque em uma lista.
#mostrar total de números, lista ordenada, se o número 5 aparece ou não e quantas vezes

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? S/N '))
    if r in 'Nn':
        break
print('=-' * 20)
print(lista)
if 5 in lista:
    print(f'O número 5 está na lista!')
else:
    print('O número 5 não aparece...')
print(f'O total de valores digitados foi: {len(lista)}')
lista.sort(reverse=True)
print(f'A lista ordenada de trás para frente: {lista}')

#fiz totalmente sozinha e está igual ao do professor