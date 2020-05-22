import math
deg = float(input('Digite o valor de um angulo: '))
degrad = math.radians(deg)
sen = math.sin(degrad)
cos = math.cos(degrad)
tan = math.tan(degrad)
print('O valo do seno é {}, do coseno é {} e da tangente é {}!'.format(sen, cos, tan))
