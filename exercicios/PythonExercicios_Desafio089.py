ficha = list()
while True:

    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()
    if opcao == 'N':
        break
print('=-' * 50)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>4}')
print('-' * 30)
for c in range(0, len(ficha)):
    print(f'{c:<4}{ficha[c][0]:<15}{ficha[c][2]:>5}')

while True:
    print('-' * 30)
    resp = int(input('Mostrar as notas de qual aluno? (999 interrompe)'))
    if resp == 999:
        break
    elif resp <= len(ficha):
        print(f'Notas de {ficha[resp][0]} são {ficha[resp][1]}')
