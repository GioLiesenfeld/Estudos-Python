menor = 0
maior = 0
for p in range (1,6):
    peso = float(input('Digite o peso da {}ª pessoa: kg '.format(p)))
    if p == 1:
        menor = p
        maior = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso lido foi kg {}\nO MENOR peso lido foi {}'.format(maior, menor))

'''muito difícil não entendi nada'''