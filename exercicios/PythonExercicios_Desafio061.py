n = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))
i = 1
while i < 11:
    print('{} '.format(n), end='')
    n += r
    i += 1