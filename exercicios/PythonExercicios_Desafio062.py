n = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))
i = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while i <= total:
        print('{} '.format(n), end='')
        n += r
        i += 1
    print('PAUSA')
    mais = int(input('Você quer mostrar mais quantos termos? '))
