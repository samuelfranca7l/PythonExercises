tot = prod1000 = cont = precobarato = 0
nomebarato = ''
while True:
    nomeproduto = str(input('Produto: '))
    preco = int(input('Preço: '))
    cont += 1
    tot += preco
    if preco > 1000:
        prod1000 += 1
    if cont == 1:
        nomebarato = nomeproduto
        precobarato = preco
    elif preco < precobarato:
        nomebarato = nomeproduto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).upper().strip()
    if opcao == 'N':
        break

print(f'O total gasto na compra foi de {tot}, {prod1000} produtos custam mais de R$1000 e o nome do produto mais '
      f'barato é {nomebarato}')

