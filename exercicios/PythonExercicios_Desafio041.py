import datetime

ano = int(input('Digite o ano em que nasceu: '))
idade = abs(datetime.datetime.today().year - ano)

if idade < 9:
    print('MIRIM')
elif idade < 14:
    print('INFANTIL')
elif idade < 19:
    print('JUNIOR')
elif idade < 20:
    print('SÊNIOR')
else:
    print('MASTER')
