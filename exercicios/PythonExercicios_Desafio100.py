from random import randint


def sorteio():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        valor = randint(1, 20)
        print(valor, end=' ')
        numeros.append(valor)


def somaPar():
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'\nSomando os valores pares de {numeros}, temos {soma}')


numeros = list()
sorteio()
somaPar()
