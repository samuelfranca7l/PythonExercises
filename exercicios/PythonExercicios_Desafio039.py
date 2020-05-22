import datetime

ano = int(input('Digite o ano em que nasceu '))
idade = datetime.datetime.today().year - ano
#print(datetime.datetime.today())
dif = abs(idade - 18)

if idade < 18:
    print('Você ainda vai se alistar. Falta(m) {} ano(s)'.format(dif))
elif idade == 18 or 17:
    print('Está na hora de se alistar')
else:
    print('já passou da hora amigao')
