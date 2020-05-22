valores = [[], []]
temp = 0
for i in range(0, 7):
    temp = (int(input(f'Digite o {i+1}º valor: ')))
    if temp % 2 == 0:
        valores[0].append(temp)
    else:
        valores[1].append(temp)
# valores.append(pares[:])
# valores.append(impares[:])
valores[1].sort()
valores[0].sort()
print(f'Os valores digitados foram {valores}')
print(f'Os valores pares digitados foram {valores[0]}')
print(f'Os valores ímpares digitados foram {valores[1]}')
