from time import sleep
for c in range(1,5): #ele não considera o último número#
    print('Hello, world!')
    sleep(1)
print('='*20)
sleep(2)
for c in range(1,6):
    print(c)
    sleep(0.5)
print('='*20)
for c in range(6, 0, -1):
    print(c)
    sleep(1)
print('='*20)
sleep(2)
n = int(input('Digite um número: '))
for c in range(1, n+1):
    print(c)
    sleep(0.5)
print('='*20)
sleep(2)
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input ('Digite o passo: '))
for c in range(i,f+1, p):
    print (c)