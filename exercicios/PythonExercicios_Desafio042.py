a = int(input('Reta 1: '))
b = int(input('Reta 2: '))
c = int(input('Reta 3: '))
if abs(c - a) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (b + a):
    if a == b and b == c:
        print('O triângulo é EQUILÁTERO')
    elif a == b or b == c or c == a:
        print('O triângulo é ISÓSCELES')
    else:
        print('O triângulo é ESCALENO')
else:
    print('O triângulo NÃO EXISTE')
