ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['média'] = float(input('Média do Aluno: '))
print(f'O nome é {ficha["nome"]}')
if ficha['média'] >= 7:
    ficha['situação'] = 'APROVADO'
    print(f'A média é {ficha["média"]}')
    print(f'Situação: {ficha["situação"]}')
else:
    ficha['situação'] = 'REPROVADO'
    print(f'A média é {ficha["média"]}')
    print(f'Situação: {ficha["situação"]}')
