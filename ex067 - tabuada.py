while True:
    c = 1
    num = int(input('Digite um número para gerar a tabuada (digite -1 para parar): '))
    if num <= 0:
        break
    while c <= 10:
        print(f'{c} x {num} = ', c*num)
        c += 1
print('Acabou!')

'''fiz sozinha'''