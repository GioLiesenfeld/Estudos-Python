lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > len(lista):
        lista.append(n)
        print('Adicionado com sucesso!')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-' * 20)
print(f'Os valores digitados foram: {list}')
#não consegui entender muito bem a lógica, o ideal seria fazer outros exercícios com o mesmo sentido