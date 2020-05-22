cont = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Número: '))
    if n != 999:
        soma += n
        cont += 1

print('Você digitou {} números e a soma deles é {}!'.format(cont, soma))
