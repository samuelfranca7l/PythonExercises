pessoas = list()
dados = list()
mai = men = 0

while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()
    if opcao == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'O maior peso foi de {mai}Kg', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(p[0])
print(f'O menor peso foi de {men}Kg', end=' ')
for p in pessoas:
    if p[1] == men:
        print(p[0])
