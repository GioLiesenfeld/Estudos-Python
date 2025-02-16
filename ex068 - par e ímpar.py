import random
vit = 0
while True:
    num = int(input('Digite um número: '))
    pi = str(input('Você deseja PAR ou ímpar [P/I]? ')).upper().strip()[0]
    x = random.randint(1,10)
    soma = num + x
    print(f'O computador escolheu {x}.')
    if soma % 2 == 0:
        print('PAR!')
        if pi in 'Pp':
            print('Você venceu!')
            vit += 1
        else:
            print('Você perdeu...')
            break
    else:
        print('ÍMPAR!')
        if pi in 'Ii':
            print('Você venceu!')
            vit += 1
        else:
            print('Você perdeu...')
            break
print(f'FIM DE JOGO! Você venceu {vit} vezes.')

#'''fiz sozinha'''