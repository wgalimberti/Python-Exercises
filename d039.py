from datetime import date
atual = date.today().year
nascm = int(input('Qual ano do seu nascimento? '))
idade = atual - nascm
print('Os nascidos em {} tem {} anos em {}'.format(nascm, idade, atual))
if idade == 18:
    print('Voce esta no ano de alistamento, dirija-se ao escritorio responsavel.')
elif idade > 18:
    print('Voce deveria ter se alistado aos 18 anos, procure o escritorio responsavel.')
else:
    print('Voce ainda nao tem a idade nescessaria, aguarde o ano em que completa 18 anos.')