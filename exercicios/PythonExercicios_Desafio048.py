soma = 0
i = 0
for c in range(1, 501):
    uni = c % 10
    dez = (c // 10) % 10
    cent = (c // 100) % 10
    #print(uni, dez, cent)
    if c % 2 != 0:
        if (uni + dez + cent) % 3 == 0:
            soma += c
            i += 1
print('A soma de todos os {} valores solicitados é {}'.format(i, soma))

