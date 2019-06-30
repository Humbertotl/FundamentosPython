print('Transformar de Farenheit para Celsius')

temp1 = float(input('Qual a temperatua em Fahrenheit?'))

#°F = °C × 1, 8 + 32

conv1 = (5 * (temp1 - 32)) / 9

print('A temperatura em Celsius e de: ', round(conv1,2),'C°')
