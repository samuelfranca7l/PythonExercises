from random import randint
sorteio = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(sorteio)
'''for c in range(0, len(sorteio)):
    if c == 0:
        maior = sorteio[c]
        menor = sorteio[c]
    if sorteio[c] > maior:
        maior = sorteio[c]
    if sorteio[c] < menor:
        menor = sorteio[c]'''
print(max(sorteio), min(sorteio))
