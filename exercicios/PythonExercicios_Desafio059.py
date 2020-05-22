from time import sleep
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('=-=' * 10)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print('A soma dos dois valores é {}!'.format(a + b))
    if opcao == 2:
        print('O produto é {}'.format(a * b))
    if opcao == 3:
        if a > b:
            print('Entre {} e {} o maior valor é {}'.format(a, b, a))
        else:
            print('Entre {} e {} o maior valor é {}'.format(a, b, b))
    if opcao == 4:
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
    if opcao > 5:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
print('=-=' * 10)
print('ECERRANDO...')
sleep(2)
prtin('FIM...')