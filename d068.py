from random import randint
v = 0
while True:
    joga = int(input('Digite um número para jogar: '))
    print(f'Você jogou {joga}')
    comp = randint(1,2)
    tota = joga + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer apostar Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'O computador jogou {comp}')
    print(f'O valor total foi {tota}')
    if tipo == 'P':
        if tota % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if tota % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente..')
print(f'Fim do jogo, Você venceu {v} vezes')
