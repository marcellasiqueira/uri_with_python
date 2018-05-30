# coding: utf-8
# URI 1015
# Distância Entre Dois Pontos
# Marcella Siqueira / discoveringpython

lista1, lista2 = raw_input().split(), raw_input().split()

x1, y1 = float(lista1[0]), float(lista1[1])

x2, y2 = float(lista2[0]), float(lista2[1])

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print "%.4f" %distancia 