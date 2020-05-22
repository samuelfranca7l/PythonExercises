matrix = [[], [], []]
for i in range(0, len(matrix)):
    for n in range(0, 3):
        matrix[i].append(int(input(f'Digite um valor para [{i},{n}]: ')))
print('=-' * 30)
for i in range(0, len(matrix)):
    for n in range(0, 3):
        print(f'[ {matrix[i][n]:^5} ]', end='')
    print('')
