from datetime import datetime


def voto(idade):
    if idade < 16:
        return print(f'Com {idade} o voto é NEGADO')
    elif 16 < idade < 18 or idade > 65:
        return print(f'Com {idade} o voto é OPCIONAL')
    else:
        return print(f'Com {idade} o voto é OBRIGATÓRIO')


print('-'*30)
ano = int(input('Digite o ano de nascimento: '))
idade = datetime.today().year - ano
voto(idade)
