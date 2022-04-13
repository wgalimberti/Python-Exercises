tot18 = mascu = femin = fem20 = 0
while True:
    nome = str(input('Nome: ')).upper().strip().split()
    idad = int(input('Idade: '))
    if idad >= 18:
        tot18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip().split()[0]
        if sexo == 'M':
            mascu += 1
        if sexo == 'F':
            femin += 1
        if sexo == 'F' and idad < 20:
            fem20 += 1
    print(f'Dados inseridos: {nome}, {sexo}, {idad}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de pessoas do sexo Masculino: {mascu}')
print(f'Total de pessoas do sexo Feminino: {femin}')
print(f'Total de pessoas do sexo Feminino menor de 20 anos: {fem20}')
print('Acabou')
