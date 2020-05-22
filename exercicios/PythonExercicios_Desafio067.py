n = cont = 0
while True:
    print('-'*30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(0, 10):
        c += 1
        print(f'{n} x {c} = {n*c}')

