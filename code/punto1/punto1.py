x = [4,9,3,2]
y = [8,17,7,4]

matriz = [
        [4,8],
        [9,17],
        [3,7],
        [2,4]
]

import statistics as st
from sklearn.preprocessing import scale, MinMaxScaler

atributo = y

# CALCULO LA MEDIA
acc = 0
for xi in x:
    acc+=xi
mean = acc / len(x)

print('MEDIA : ' + str(mean))

# CALCULO DEL DESVIO ESTANDAR

sd = st.stdev(atributo)

x_zscore = list()

for valor in atributo:
    x_zscore.append((valor-mean)/sd)

print(x_zscore)

import scipy.stats as stats
import numpy as np

data = np.array(atributo)

print(stats.zscore(matriz))

matriz = scale(matriz)
print("Matriz escalada por ZScore")
print(matriz)

from sklearn.cluster import KMeans

# Por defecto usa la distancia euclidea
km = KMeans(
    n_clusters=3, init='random',
    n_init=10, random_state=0
)

print(matriz[0:3])
print(matriz[3:])

from scipy.spatial import distance

result = list()
result1 = list()
result2 = list()

print("DISTANCIA Euclidean")
for xi in matriz[0:3]:
    dst = distance.euclidean(xi,matriz[3:])
    result.append(dst)
print(result)
print("DISTANCIA Minkowski")
for xi in matriz[0:3]:
    dst = distance.minkowski(xi,matriz[3:],3)
    result1.append(dst)
print(result1)
print("DISTANCIA Manhattan")
for xi in matriz[0:3]:
    dst = distance.cityblock(xi,matriz[3:])
    result2.append(dst)
print(result2)
