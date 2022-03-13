dist = float(input('Qual a distancia da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {} km.'.format(dist))
if dist <= 200:
    prec = dist * 0.50
else:
    prec = dist * 0.45
print('E o preco da sua passagem sera de R$ {:.2f}'.format(prec))