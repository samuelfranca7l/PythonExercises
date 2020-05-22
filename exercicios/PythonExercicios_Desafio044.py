preco = float(input('Qual é o preço do produto: '))

print('Qual é a forma de pagamento?')

pag = int(input('1 - À VISTA, DINHEIRO OU CHEQUE \n2 - À VISTA NO CARTAO \n3 - EM ATÉ 2X NO CARTAO \n4 - '
                '3X OU MAIS NO CARTAO '))

if pag == 1:
    print('Valor a ser pago: {}'.format(preco*0.9))
elif pag == 2:
    print('Valor a ser pago: {}'.format(preco*0.95))
elif pag == 3:
    print('Valor a ser pago: {}'.format(preco))
elif pag == 4:
    print('Valor a ser pago: {}'.format(preco*1.2))
else:
    print('Valor Inválido')
