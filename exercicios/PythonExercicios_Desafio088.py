from random import sample
from time import sleep
jogo = list()
print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
opcao = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(0, opcao):
    jogo = sorted(sample(range(1, 60), 6))
    print(jogo)
    sleep(1)

# from random import sample
# from time import sleep
# jogos=list()
# n=int(input('Quantos jogos?: '))
# for c in range(n):
#   a=sorted(sample(range(1, 61), 6))
#   jogos.append(a[:])
#   print(f'Jogo {c+1}: {a}')
#   sleep(0.5)