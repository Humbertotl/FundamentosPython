
valores = []
condicao = True
while condicao:
    for _ in range(5):
        valores.append(int(input('Digite um numero: ')))
        print()
    print ('O maior numero é: ', max(valores))
    sair = input('Deseja repetir? sim ou não')
    if sair == 'sim':
        continue
    else:
        break
