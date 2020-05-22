lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = 'a'
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()
    if opcao == 'N':
        break
for c in range(len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print(lista)
print(pares)
print(impares)
