expressao = str(input(('Digite uma expressão: ')))
lista = []
for i in range(0, len(expressao)):
    lista.append(expressao[i])
if lista.count('(') == lista.count(')'):
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
