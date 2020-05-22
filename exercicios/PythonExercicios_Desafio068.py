from random import randint
jogador = computador = i = soma = 0
parouimpar = ''
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + computador
    parouimpar = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. ', end='')
    if parouimpar == 'P':
        if soma % 2 == 0:
            print(f'Total de {soma} DEU PAR')
            print('-' * 30)
            print('Você VENCEU!\nVamos jogar novamente...\n', '=-'*15)
        if soma % 2 != 0:
            print(f'Total de {soma} DEU ÍMPAR')
            print('-' * 30)
            print('Você PERDEU!')
            break
        i += 1
print(f'GAME OVER! Você venceu {i} vezes.')