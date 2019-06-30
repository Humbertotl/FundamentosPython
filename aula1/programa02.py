print('Digite o numero de faltas: ' )

fre_1 = int(input('Digite o total de aulas: '))
fal_1 = int(input('Digite o total de faltas: '))

frequencia = (fre_1-fal_1)

print ('Frequencia do aluno e: ' + srt(frequencia))

if frequencia >= 7:
    print()

print ('Digite as notas.')

num1 = float(input ('Digite a primeira nota: '))
num2 = float(input ('Agora a segunda nota: '))

media = (num1+num2)/2

print ('Media igual: ' + str(media))

if media >= 7:
    print('Aluno APROVADO e sua media e: ' + str(media))

elif 3 < media < 7:
    print ('O Aluno esta em RECUPERACAO')

elif media < 3:
    print('O Aluno esta REPROVADO!')

else:
    print('O Aluno esta REPROVADO!')



