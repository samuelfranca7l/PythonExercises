import random
computador = random.randint(1, 11)
jogador = int(input('Digite um número: '))
cont = 1
while jogador != computador:
    jogador = int(input('Digite um número: '))
    cont += 1
print('O COMPUTADOR JOGOU {}'.format(computador))
print('O JOGADOR JOGOU {}'.format(jogador))
print('Você tentou {} vez(es) até acertar!'.format(cont))
