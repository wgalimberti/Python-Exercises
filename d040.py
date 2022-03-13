n1 = float(input('Digite a PRIMEIRA nota: '))
n2 = float(input('Digite a SEGUNDA nota: '))
media = (n1 + n2) / 2
print('A MEDIA das duas notas eh {}'.format(media))
if media <= 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')
else:
    print('RECUPERACAO')
