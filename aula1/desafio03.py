print('Ordem decrescente: ')

num1 = int(input ('Digite o primeiro numero: '))

num2 = int(input ('Digite o segundo numero: '))

num3 = int(input ('Digite o terceiro numero: '))

if num1 > num2 > num3:
    print(num3, num2, num1)
if num3 > num2 > num1:
    print(num1, num2, num3)
if num2 > num3 > num1:
    print(num1, num3, num2)
if num2> num1 > num3:
    print(num3, num1, num2)

