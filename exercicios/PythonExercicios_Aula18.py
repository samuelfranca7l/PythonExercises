"""teste = list()
teste.append('Samuel')
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = '40'
galera.append(teste[:])
print(galera)"""

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''
#
# galera = list()
# dados = list()
# for i in range(0,3):
#     dados.append(str(input('Nome: ')))
#     dados.append(int(input('Idade: ')))
#     galera.append(dados[:])
#     dados.clear()
# # print(galera)
# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade')
#     else:
#         print(f'{p[0]} é menor de idade')

# matrix = [[1,2,3], [1,2,3], [1,2,3]]
# print(matrix[1][2])

notas = [2,4]
a = sum(notas)
b = len(notas)

print(a/b)
