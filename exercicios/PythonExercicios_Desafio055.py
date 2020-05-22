gordo = 0
magro = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        gordo = peso
        magro = peso
    else:
        if peso > gordo:
            gordo = peso
        if peso < magro:
            magro = peso

print(magro, gordo)
