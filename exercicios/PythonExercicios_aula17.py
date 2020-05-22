'''num = [2, 3, 7, 1]
num[2] = 4
num.append(6)
num.insert(1, 6)
# num.sort(reverse=True)
# num.pop(2)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Nao achei o numero 4')
print(f'Essa lista tem {len(num)} elementos')
print(num)
'''

'''valores = []

for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao fim da lista')'''

'''a = [2, 3, 4, 7]
b = a
b[2] = 8
print(a, b)
QUANDO EU IGUAL UMA LISTA A OUTRA, É FEITA UMA LIGAÇÃO ENTRE ELAS, DESSA FORMA, QUANDO ALTERO O ELEMENTO 2 DO B, TAMBEM
SE ALTER O ELE MENTO 2 DA LISTA A.'''

'''a = [2, 3, 4, 7]
b = a[:] AQUI ESTOU COPIANDO A LISTA, E NÃO LINKANDO UMA A OUTRA
b[2] = 8
print(a, b)
'''