soma = 0
for c in range(0, 6):
    n = int(input('Número: '))
    if n % 2 == 0:
        soma += n
print('A soma é {}'.format(soma))
