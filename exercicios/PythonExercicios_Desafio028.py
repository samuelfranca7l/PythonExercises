import random
from time import sleep
n = int(random.randint(0, 5))
n1 = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if n1 == n:
    print('Acertou!')
else:
    print('Errou!')
print('O número sorteado foi {}!'.format(n))

