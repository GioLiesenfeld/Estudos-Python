#programa que gere 5 números aleatórios e coloque-os em tupla
from random import randint
num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores sorteados foram {num}')
print(f'O maior valor é {max(num)}')
print(f'O menor valor é {min(num)}')
#precisei assistir o vídeo, não havia ensinado em aulas, ensinado diretamente no exercício