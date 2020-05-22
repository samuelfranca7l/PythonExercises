igenderM = iage18 = iFemaleAge20 = 0
opcao = ''
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()
    if sexo == 'M':
        igenderM += 1
    if idade > 18:
        iage18 += 1
    if sexo == 'F':
        if idade < 20:
            iFemaleAge20 += 1
    opcao = str(input('Deseja continuar? [S/N]')).upper().strip()
    if opcao == 'N':
        break
    while opcao != 'S':
        opcao = str(input('Deseja continuar? [S/N]')).upper().strip()

print(f'''Foram cadastradas {iage18} pessoas maiores de 18 anos, {igenderM} homens e {iFemaleAge20} mulheres menores 
de 20 anos''')
print('FIM DO JOGO')
