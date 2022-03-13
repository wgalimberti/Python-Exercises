peso = float(input('Peso em Kilogramas: '))
altura = float(input('Altura em Centimetros: '))
imc = peso / ((altura / 100) ** 2)
print('O IMC esta em {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso!')
elif imc <= 25:
    print('Peso Ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Morbida')
