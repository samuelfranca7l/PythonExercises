cont = soma = media = maior = menor = 0
opcao = str('s')
n = 0
while opcao not in 'Nn':
    if opcao in 'Ss':
        n = int(input('Digite um número: '))
        soma += n
        cont += 1
        opcao = str(input('Quer continuar? [S/N] '))
    if opcao not in 'SsNn':
        opcao = str(input('Opção inválida, digite [S/N] '))
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / cont
print(maior, menor)
print(media)
