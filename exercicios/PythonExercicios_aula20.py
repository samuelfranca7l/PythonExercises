'''def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


# Programa Principal
mensagem('Samuel')
'''


'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} com {b} é {s}')


# Programa Principal
soma(b=4, a=8)
# soma(5, 10)
# soma(2, 1)'''


'''def contador(*núm):
    for valor in núm:
        print(valor, end=' ')
    print('FIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
