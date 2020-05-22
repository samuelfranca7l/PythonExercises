def fatorial(num, show=False):
    f = 1
    for c in range(num, 1, -1):
        f *= c
        if show:
            print(f, end=' ')
    print(f)


print('-' * 30)
fatorial(5, show=True)
