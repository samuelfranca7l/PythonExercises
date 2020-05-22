valores = []

while True:
    v1 = int(input('Digite um valor: '))
    if v1 in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(v1)

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar ? [S/N]')).strip().upper()
    if opcao == 'N':
        break
print('=-' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
