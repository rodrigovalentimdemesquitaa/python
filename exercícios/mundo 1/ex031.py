distancia = float(input('Qual é a distância da sua viagem: '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('Você está prestes a começar uma viagem de {:.2f}km'.format(distancia))
print('E o preço da passagem será de R${:.2f}'.format(valor))