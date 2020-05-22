n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1+n2)/2

if media < 5.0:
    print('Você está \033[31mREPROVADO!')
elif media < 6.9:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você foi APROVADO!')