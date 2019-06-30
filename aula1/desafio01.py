print('Qual o maior numero?')
maior = 0

num1 = int(input ('Digite o primeiro numero: '))
if num1 > maior:
    maior = num1

num2 = int(input ('Digite o segundo numero: '))
if num2 > maior:
    maior = num2

num3 = int(input ('Digite o terceiro numero: '))
if num3 > maior:
    maior = num3

num4 = int(input ('Digite o quarto numero: '))
if num4 > maior:
    maior = num4

num5 = int(input ('Digite o quinto numero: '))
if num5 > maior:
    maior = num5

print('Esse e o maior: ' + str(maior))
