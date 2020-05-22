def notas(*notas, sit=False):
    quant = len(notas)
    maior = menor = soma = 0
    for c in range(0, len(notas)):
        if c == 0:
            maior = notas[0]
            menor = notas[0]
        else:
            if notas[c] > maior:
                maior = notas[c]
            if notas[c] < menor:
                menor = notas[c]
        soma += notas[c]
    media = soma / len(notas)
    if media < 5:
        sit = 'RUIM'
    elif 5 < media < 7:
        sit = 'RAZOAVEL'
    else:
        sit = 'BOM'
    if sit == True:
        return {'Quantidade': quant,
                'Maior': maior,
                'Menor': menor,
                'Média': media,
                'Situação': sit}
    else:
        return {'Quantidade': quant,
                'Maior': maior,
                'Menor': menor,
                'Média': media}


resp = notas(1, 3, 2, 5, sit=False)
print(resp)
