salar = float(input('Qual valor do salario? R$ '))
casa = float(input('Qual valor da casa? R$ '))
anos = int(input('Quantos anos deve ter o financiamento? '))
minim = salar * 30 / 100
prest = casa / (anos * 12)
print('O pagamento do Imovel de R${:.2f} em {} anos a prestacao sera de R${:.2f}'.format(casa, anos, prest))
if prest <= minim:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO!')
