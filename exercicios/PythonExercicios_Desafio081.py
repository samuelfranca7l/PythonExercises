numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números')
print(f'a ordem decrescente da lista é {numeros}')
if 5 in numeros:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
