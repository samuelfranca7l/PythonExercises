import random
nome1 = input('Nome 1')
nome2 = input('Nome 2')
nome3 = input('Nome 3')
nome4 = input('Nome 4')
sorteio = random.sample([nome1, nome2, nome3, nome4], k=4)
print('A sequência é {}'.format(sorteio))
