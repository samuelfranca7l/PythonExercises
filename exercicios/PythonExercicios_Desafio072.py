extenso = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Quatorze', 'Quinze', 'Dezesseis,', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numero = 0

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('Número inválido. Digite um número entre 0 e 20: '))
    print(extenso[numero-1])
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).upper().strip()
    if opcao == 'N':
        break
