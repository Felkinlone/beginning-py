from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}' .format(ang, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(ang, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}' .format(ang, tan))
