n = int(input('Digite um número: '))
count = 0
for c in range(1, n+1):
    if n % c != 0:
        print('\033[031m', c, '\033[m', end='')
    else:
        print('\033[033m', c, '\033[m', end='')
        count += 1
if count == 2:
    print('\n O número {} foi divisível {} vezes \n E por isso ele É UM PRIMO'.format(n, count))
else:
    print('\n O número {} foi divisível {} vezes \n E por isso ele NÃO É UM PRIMO'.format(n, count))
