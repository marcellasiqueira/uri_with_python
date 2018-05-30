# coding: utf-8
# URI 1013
# O Maior
# Marcella Siqueira / discoveringpython

lista = raw_input().split()

a, b, c = int(lista[0]), int(lista[1]), int(lista[2])

maiorAB = (a + b + abs(a - b)) / 2

maiorABC = (maiorAB + c + abs(maiorAB - c)) / 2

print "%i eh o maior" %maiorABC