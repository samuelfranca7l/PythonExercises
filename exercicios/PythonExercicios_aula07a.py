n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a multiplicação é {}, a divisão é {:.7f}'.format(s, m, d), end='')
print('a divisão inteira é {} e a exponenciação é {}!'.format(di, e))
