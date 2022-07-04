from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
computador = randint(0, 5)
jogador = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(1)
if jogador == computador:
    print('\033[34mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}\033[m'.format(computador, jogador))