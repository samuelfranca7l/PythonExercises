def area(a, b):
    print(f'A área de um terreno {a}x{b} é de {a*b}m²')


print(f'{"CONTROLE DE TERRENO":^30}')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
