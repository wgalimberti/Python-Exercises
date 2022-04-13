valor = int(input('Valor do Saque: R$ '))
total = valor
cedul = 50
totced = 0
while True:
    if total >= cedul:
        total -= cedul
        totced += 1
    else:
        print(f'Total de {totced} cédulas de R$ {cedul}')
        if cedul == 50:
            cedul = 20
        elif cedul == 20:
            cedul = 10
        elif cedul == 10:
            cedul = 1
        totced = 0
        if total == 0:
            break
print('Fim!')
