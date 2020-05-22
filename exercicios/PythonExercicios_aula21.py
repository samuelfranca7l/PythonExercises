# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: início da contgem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     Função criada por Samxiii - HackersMaster
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end=' ')
#         c += p
#     print('FIM')
#
#
# help(contador)
# contador(2, 10, 2)


'''def somar(a, b, c=0):  # parâmetro opcional
    s = a + b + c
    print(f'A soma é {s}')


somar(2, 3)'''

# def teste():
#     x = 8
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')
#
# teste()
# n = 2

f = 1
num = 5
for c in range(num, 1, -1):
    f *= c
    print(f)
