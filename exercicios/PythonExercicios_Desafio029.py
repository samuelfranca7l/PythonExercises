vel = int(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Normal')
else:
    print('O valor da multa é de {}'.format(multa))
