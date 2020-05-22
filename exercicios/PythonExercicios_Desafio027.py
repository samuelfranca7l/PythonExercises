nome = str(input('Digite seu nome completo: ')).strip()
listanome = nome.split()
print('Seu primeiro nome é {}'.format(listanome[0]))
print('Seu último nome é {}'.format(listanome[len(listanome)-1]))
