frase = str(input('Digite uma frase: ')).strip().upper()
frase = ''.join(frase.split())
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
print (frase, inverso)
if inverso == frase:
    print('Essa frase é um Palíndromo')
