peso = float(input('Digite seu Peso: '))
altura = float(input('Digite sua Altura: '))

imc = peso / altura**2

print('Seu IMC é {:.2f} '.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
