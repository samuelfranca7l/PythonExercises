def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            print(f'Valor válido: {valor}')
        else:
            print('\033[0;31mValor inválido, digite novamente: \033[m')
        if ok:
            break
    return valor


leiaInt('Digite um número: ')