soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        cont = cont + 1
print('O resultado da soma dos {} numeros eh {}'.format(cont, soma))
