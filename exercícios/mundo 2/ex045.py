from random import randint
from time import sleep
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
computador = randint(1,3)
jogador = int(input('Qual é a sua jogada? ' ))
print('\33[31mJO')
sleep(1)
print(f'{"KEN":>7}')
sleep(1)
print(f'{"PO!!!":>14}\033[m')
print('-='*10)
print('Computador jogou {} '.format(computador))
print('Jogador jogou {}'.format(jogador))
print('-='*10)
if computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 2:
        print('JOGADOR VENCE')
    elif jogador == 3:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # COMPUTADOR JOGOU PAPEL
    if jogador == 3:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
       print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
else:
    if jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    elif jogador == 3:
        print('EMPATE')


