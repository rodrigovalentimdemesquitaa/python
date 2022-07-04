print('-='*15)
print('Analisador de Triãngulos')
print('-='*15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Os segmentos acima PORDEM FORMAR triãngulo!')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triãngulo')
