tot = 0
num = int(input('Digite um número: '))
for primo in range(1, num+1):
    if num % primo == 0:
        tot += 1
        print('\033[31m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(primo), end='')
print('\n\033[mO número {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')