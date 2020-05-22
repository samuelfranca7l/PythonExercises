valor = int(input('Qual é o valor da casa? '))
salario = int(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos pretende financiá-la? '))

meses = anos * 12
mensal = valor / meses
percent = (0.3 * salario)

print('O valor da parcela é {:.0f}'.format(mensal))
print('30% do salário representa {:.0f}'.format(percent))

if mensal >= percent:
    print('Como {:.0f} é maior que {:.0f}: empréstimo negado. '.format(mensal, percent))
else:
    print('Como {:.0f} é menor que {:.0f}: empréstimo concedido. '.format(mensal, percent))
