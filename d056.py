somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'{p} Pessoa')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media de idade eh de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos.')
