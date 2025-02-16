#criar uma tupla com palavras e coletarr somente as vogais

palavras = ('aprender', 'ler', 'estudar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end= ' ')
    for letra in p:
        if letra.lower() in 'aâãeéêiou':
            print(letra, end= ' ')

#precisei de ajuda do vídeo