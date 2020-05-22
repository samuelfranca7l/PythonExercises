import math
cop = float(input('Insira o comprimento do cateto oposto: '))
cadj = float(input('Insira o comprimento do cateto adjacente: '))
#hipo = math.sqrt(math.pow(cop, 2)+math.pow(cadj, 2))
print('O comprimento da hipotenusa é {}'.format(math.sqrt(math.pow(cop, 2)+math.pow(cadj, 2))))

