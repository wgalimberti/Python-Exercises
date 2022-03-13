from datetime import date
hoje = date.today().year
totmaior = 0
totmenor = 0
print('Ano atual {}'.format(hoje))
for pess in range(1, 8):
    nasc = int(input('Diga o ano de nascimento: '))
    idad = hoje - nasc
    if idad >= 18:
            totmaior += 1
    elif idad <= 18:
            totmenor += 1
print('{} sao menores de idade.'.format(totmenor))
print('{} sao maiores de idade.'.format(totmaior))