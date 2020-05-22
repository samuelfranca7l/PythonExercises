sal = int(input('Digite o seu salário: '))
if sal >= 1250:
    sal = (sal*1.1)
else:
    sal = sal*1.15
print('O valor do salário com aumento é de {}'.format(sal))
