perguntas = ['Digite o primeiro numero: ', 'segundo: ', 'terceiro: ','quarto: ','quinto: ']
respostas = []

for pergunta in perguntas:
    respostas.append(input(pergunta))

perguntas_respostas = zip(perguntas, respostas)

print()

print (list(perguntas_respostas))

print()

maior_numero = sorted(respostas, reverse=True)

print('Esse e o maior: ' + str(maior_numero[0]))




#######################################


valores = []

for _ in range(5):
    valores.append(int(input('Digite um numero: ')))
    print()

print ('O maior numero é: ', max(valores))


