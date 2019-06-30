#palavras = ['Oi','tudo','bem','com','voce']

#for palavra in palavras:
	    #print(palavra)


#for numero in range(10):
    #print(numero)

#for numero in range(10):
    #print('oi')

#########################################



#lista_nomes = []

#for _ in range(5):
    #lista_nomes.append(input('Digite um nome: '))



#print(lista_nomes)


##############################################

perguntas = ['Qual e o seu nome? ','Qual a sua idade? ','Qual e a sua profissao? ']
respostas = []


if type(perguntas)!=int:
    print ('ERRO')
else:
    print ('E INTEIRO')

for pergunta in perguntas:
    respostas.append(input(pergunta))



#print(perguntas)
#print(respostas)

perguntas_respostas = zip(perguntas, respostas)

print (list(perguntas_respostas))
