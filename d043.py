produto = float(input('Digite o valor do produto R$'))
print('''
1 - Pagamento a vista Dinheiro / Cheque: 10% desconto
2 - Pagamento a vista no cartao de Debito: 5% desconto
3 - Pagamento em 2x no cartao de Credito: preco normal
4 - Pagamento em 3x ou mais no cartao de Credito: 20% de juros
''')
pagamento = int(input('Digite a forma de pagamento desejada: '))
if pagamento == 1:
    total = produto - (produto * 10 / 100)
elif pagamento == 2:
    total = produto - (produto * 5 / 100)
elif pagamento == 3:
    total = produto
    parcela = total / 2
    print('O produto sera parcelado em 2x de R${}'.format(parcela))
elif pagamento == 4:
    total = produto * 1.2
    tparcela = int(input('Quantas parcelas? '))
    parcela = total / tparcela
    print('O produto sera parcelado em {}x de R${}'.format(tparcela, parcela))
print('Conforme a opcao de pagamento escolhida, o produto de R${} vai custar R${}.'.format(produto, total))
