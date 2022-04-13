vrtot = vr01k = vrmen = volum = 0
barat = ' '
while True:
    produ = str(input('Nome do produto: ')).upper().strip().split()
    vrprd = float(input('Valor do produto: R$ '))
    volum += 1
    vrtot += vrprd
    if vrprd >= 1000:
        vr01k += 1
    if volum == 1 or vrprd < vrmen:
        vrmen = vrprd
        barat = produ
    respo = ' '
    while respo not in 'SN':
        respo = str(input('Continuar? [S/N]')).strip().upper()[0]
    if respo == 'N':
        break
print('Terminou!')
print(f'O valor total foi R$ {vrtot:.2f}')
print(f'A quantidade de produtos custando mais de mil reais foi: {vr01k}')
print(f'O produto mais barato custa R$ {vrmen:.2f}')
print(f'O produto mais barato foi {barat}')
