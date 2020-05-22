import datetime
ano20 = datetime.datetime.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    if ano20 - ano >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade e {} ainda nao atingiram a maioridade!'.format(maior, menor))
