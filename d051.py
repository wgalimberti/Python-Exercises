frase = str(input('Digite a frase para verificar: ')).strip().upper()
palav = frase.strip()
junto = ''.join(palav)
inver = ''
for letra in range(len(junto) - 1, -1, -1):
    inver += junto[letra]
if inver == junto:
    print('Palindromo!')
else:
    print('Nao eh um Palindromo!')
