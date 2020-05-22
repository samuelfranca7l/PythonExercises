print('=' * 30)
print('{:^30}'.format('BANCO SAMXO'))
print('=' * 30)
valor = int(input('Qual é o valor a ser sacado? '))
cedula = 50
total = valor
icedula = 0
while True:
    if total >= cedula:
        total -= cedula
        icedula += 1
    else:
        if icedula > 0:
            print(f'Total de {icedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break
        icedula = 0
