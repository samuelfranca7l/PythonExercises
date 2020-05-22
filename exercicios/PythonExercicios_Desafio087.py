matrix = [[], [], []]
somap = somacol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))
        if matrix[l][c] % 2 == 0:
            somap += matrix[l][c]
for l in range(0, 3):
    somacol += matrix[l][2]
for c in range(0, 3):
    if c == 0:
        maior = matrix[1][0]
    elif matrix[1][c] > maior:
        maior = matrix[1][c]
print('=-' * 30)
for i in range(0, 3):
    for n in range(0, 3):
        print(f'[ {matrix[i][n]:^5} ]', end='')
    print('')
print('=-' * 30)
print(f'A soma dos valores pares é {somap}')
print(f'A soma dos valores da terceira coluna é {somacol}')
print(f'O maior valor da sgunda linha é {maior}')
