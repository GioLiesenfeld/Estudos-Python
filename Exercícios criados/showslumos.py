#calculadora de cachê em relação ao número de shows por mês

nshows = int(input('Digite o número de shows para o mês: '))
cache = float(input('Digite o chachê que irá cobrar: '))
cachetot = nshows * cache
print(f'Com {nshows} e cobrando R${cache}, total será R${cachetot}')