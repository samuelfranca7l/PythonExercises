numeros = (int(input('1º Número: ')),
           int(input('2º Número: ')),
           int(input('3º Número: ')),
           int(input('4º Número: ')))

print(f'Você digitou os números {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 está na posição {numeros.index(3) + 1}')
else:
    print('O valor 3 não foi digitado')

print(f'Os valores pares digitados foram', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
