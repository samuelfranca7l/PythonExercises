from datetime import datetime
funcionario = dict()
funcionario['nome'] = str(input('Nome: ')).strip()
anonasc = int(input('Ano de Nascimento: '))
funcionario['idade'] = datetime.today().year - anonasc
funcionario['ctps'] = int(input('Número da CTPS: '))
if funcionario['ctps'] != 0:
    funcionario['contratacao'] = int(input('Ano de contratação: '))
    funcionario['salario'] = int(input('Salário: R$'))
    funcionario['aposentadoria'] = funcionario['contratacao'] + 35 - datetime.now().year + funcionario['idade']
else:
    print('Pessoa sem carteira de trabalho!')
    print(f'{"FIM":-^30}')
print('=-' * 30)
print(funcionario)
for k, v in funcionario.items():
    print(f'{k} tem o valor {v}')

