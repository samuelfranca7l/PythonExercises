from time import sleep


def lin():
    print('=-' * 20)


def contador(inicio, fim, passo):
    lin()
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    if passo == 0:
        passo = 1
    if inicio < fim:
        while fim >= inicio:
            print(inicio, end=' ')
            inicio += passo
            sleep(0.5)
    elif fim < inicio:
        while fim <= inicio:
            print(inicio, end=' ')
            inicio -= abs(passo)
            sleep(0.5)
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)

lin()
print('AGORA É A SUA VEZ!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
