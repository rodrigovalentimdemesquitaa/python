from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} de o seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} de o cosseno de {:.2f}'.format(angulo, cosseno))
tagente = tan(radians(angulo))
print('O ângulo de {} de o tagente de {:.2f}'.format(angulo, tagente))

