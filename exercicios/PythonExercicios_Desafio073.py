times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlhetico-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',
         'Chapecoense', 'Avaí')
print('=-' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('=-' * 30)
print(f'Os 5 primeiros são {times[:5]}')
print('=-' * 30)
print(f'Os 4 últimos são {times[16:]}')
print('=-' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-' * 30)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª Posição')