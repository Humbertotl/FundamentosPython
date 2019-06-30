
#Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print ('Alo mundo')

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

num1 = int(input('Digite um numero: '))

print ('O numero informado foi: ', num1 )

#Faça um Programa que peça dois números e imprima a soma.

num2 = int(input('Digite um numero: '))

num3 = int(input('Digite outro numero: '))

soma = int(num2) + int(num3)

print ('A soma é:', soma)

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('Digite as 4 notas')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1+num2+num3+nota4) / 4

print ('A media do aluno foi: ', str(media))

#Faça um Programa que converta metros para centímetros.

print('Converta de metros para centimetros')

metr1 = float(input('Digite o nomero em metros: '))

conver = (metr1 / 100)

print ('Então:',metr1, 'metros convertito para centimetro fica:', conver,'cm.')

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


print ('Calcule a area do circulo')

circ1 = float(input('Qual o raio do ciculo: '))

are1 = (circ1*circ1) * 3.14

print ('A area do ciculo e: ', are1, 'cm²')

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print('Calcule a area de um quadrado')

quadr1 = float(input('Digite a area do quadrado: '))

totarea = int(quadr1)*int(quadr1)

print ('A area total do quadrado e de:', totarea ,'cm²!' )

dobro1 = (totarea)*2

print('Dobro da area e:', dobro1 )

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print('calculo de salario mensal')

vphora = float(input('Digite o valor da sua hora de trabalho: '))
hpdia = float(input('Digite quantas horas por dia você trabalha: '))
diaspmes = float(input('Digite quantos dias voce trabalha por mes: '))

salatot = (vphora) * (hpdia) * (diaspmes)

print('Voce recebera no fim do mes a quantia de: ', 'R$',salatot )

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

print('Transformar de Farenheit para Celsius')

temp1 = float(input('Qual a temperatua em Fahrenheit?'))

conv1 = (5 * (temp1 - 32)) / 9

print('A temperatura em Celsius e de: ', round(conv1,2),'C°')


