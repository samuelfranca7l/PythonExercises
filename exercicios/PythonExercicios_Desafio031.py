dist = int(input('Digite a distância em KM: '))
if dist <= 200:
    print('O preço da passagem é {}'.format(0.5*dist))
else:
    print('O preço da passagem é {}'.format(0.45*dist))
