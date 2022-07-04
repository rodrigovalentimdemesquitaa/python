times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Framengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-='*15)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabéticas {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')
