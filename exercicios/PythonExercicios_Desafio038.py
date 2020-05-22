n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('{} é o maior valor'.format(n1))
elif n2 > n1:
    print('{} é o maior valor'.format(n2))
else:
    print('Nenhum valor é maior, os dois são iguais! ')
