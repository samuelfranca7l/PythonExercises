jogador = dict()
somagols = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas Partidas {jogador["nome"]} jogou? '))
jogos = list()
for g in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {g+1}? '))
    somagols += gols
    jogos.append(gols)

jogador['gols'] = jogos
jogador['total'] = somagols
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for p, g in enumerate(jogos):
    print(f'Na partida {p} fez {g} gols')
