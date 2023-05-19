w = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
area = w*h
tinta = area/2
print('Dimensão da parede de {}x{} e sua área é de {}m²'.format(w, h, area))
print('Para pintar essa parede voce precisara de {}L de tinta'.format(tinta))
