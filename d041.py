from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade: int = atual - nascimento
print('O atleta nascido em {} atualmente tem {} anos.'.format(nascimento,idade))
if idade <= 9:
    print('Classificacao MIRIM')
elif idade <= 14:
    print('Classificacao INFANTIL')
elif idade <= 19:
    print('Classificacao JUNIOR')
elif idade <= 25:
    print('Classificacao SENIOR')
else:
    print('Classificacao MASTER')
