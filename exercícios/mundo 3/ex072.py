#NÃO ESTOU CONSEGUINDO...

numeros = ('zero', 'um', 'dois', 'três',
           'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quartoze', 'quinze',
           'dezesseis','dezessete', 'dezoito', 'dezenove',
           'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'você digitou o número {numeros[num]}')
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Deseja continuar? ')).strip().upper()[0]
            if resposta in 'S':
                print('Ok! Então...', end=' ')
                break
        if resposta in 'N':
            print('Hummm... ')
            break
print('Obrigado então. TCHAU!')



