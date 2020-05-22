def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato!')


# Programa Principal
a = str(input('Nome do Jogador: '))
b = str(input('Gols: '))
if b.isnumeric():
    b = int(b)
else:
    b = 0
if a.strip() == '':
    ficha(gols=b)
else:
    ficha(a, b)

