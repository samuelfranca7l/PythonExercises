a = int(input('Reta 1: '))
b = int(input('Reta 2: '))
c = int(input('Reta 3: '))
if abs(c - a) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (b + a):
    print('O triângulo existe')
else:
    print('O triângulo não existe')
