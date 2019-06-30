lista = ['Humberto', 'Johanna', 'Lucca','Bolota',]

print(lista)

lista_sobrenome = ['lima', 'odebrecht', 'dias','dog']

list_idade = [22,32,1,3]

#lista.extend([1,2])

#lista += [1,2]

lista.extend (lista_sobrenome + list_idade)
print('concatenacao')

lista += ['arvore',123,True]

print(lista, 'final')
