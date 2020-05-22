import random
import time
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
computador = random.randint(0, 2)
print('JO...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('PO!!!')
print('-=' * 14)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 14)