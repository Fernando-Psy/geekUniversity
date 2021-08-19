# d² = x² + y²
# d = sqrt(x² + y²)

from math import sqrt

x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de x: '))

distancia = sqrt((x - y) ** 2)
print(f'A distância de origem é: {distancia}')
