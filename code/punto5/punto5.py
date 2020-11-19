import pandas as pd 

# Lee el archivo
data = pd.read_csv(r"code\punto5\ds-abandono.csv") 
# Preview the first 5 lines of the loaded data 

# print(data.columns)

x = data[([
           'horas_trabajadas',
           'edad_ingreso',
           'colegio_publico',
           'aprobadas_1er_anio',
           'c_promociones_1er_anio',
           'c_libres_1er_anio',
           'c_regulares_1er_anio',
           'c_ausentes_1er_anio',
           'c_noausentes_1er_anio',
           'cursadas_ap_1er_anio',
           'cursadas_1er_anio',
           'cambio_universidad',
           'fracaso_academico',
           ])]

df = pd.DataFrame(x)  
df.to_csv(r'code\punto5\filtrado.csv')

from sklearn.preprocessing import scale, MinMaxScaler

scaled_1 = scale(x)

from sklearn.cluster import KMeans

# Por defecto usa la distancia euclidea
km = KMeans(
    n_clusters=2, init='random',
    n_init=20, random_state=0
)

y_km = km.fit_predict(scaled_1)

# print(y_km)

# print(km.cluster_centers_)

# print(scaled_1)

# df = pd.DataFrame(km.cluster_centers_)   
# df.to_csv(r'code\punto5\centroides.csv')

# df = pd.DataFrame(scaled_1[y_km == 0])   
# df.to_csv(r'code\punto5\cluster_0.csv')
# df = pd.DataFrame(scaled_1[y_km == 1])   
# df.to_csv(r'code\punto5\cluster_1.csv')
# df = pd.DataFrame(scaled_1[y_km == 2])   
# df.to_csv(r'code\punto5\cluster_2.csv')

df = pd.DataFrame(y_km)   
df.to_csv(r'code\punto5\y_km.csv')


import matplotlib.pyplot as plt

# #configuro el tamaño del grafico final
# plt.figure(figsize=(10,7))

# #scatter del primer cluster
# plt.scatter(
#     scaled_1[y_km == 0, 0], scaled_1[y_km == 0, 1],
#     s=50, c='lightgreen',
#     marker='s', edgecolor='black',
#     label='cluster 1'
# )
# #scatter del segundo cluster
# plt.scatter(
#     scaled_1[y_km == 1, 0], scaled_1[y_km == 1, 1],
#     s=50, c='orange',
#     marker='o', edgecolor='black',
#     label='cluster 2'
# )
# # scatter del tercer cluster
# plt.scatter(
#     scaled_1[y_km == 2, 0], scaled_1[y_km == 2, 1],
#     s=50, c='lightblue',
#     marker='v', edgecolor='black',
#     label='cluster 3'
# )
# # scatter del los centroides
# plt.scatter(
#     km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
#     s=250, marker='*',
#     c='red', edgecolor='black',
#     label='centroides'
# )
# # le pongo la leyenda
# plt.legend(scatterpoints=1)
# # hace una grilla en el grafico
# plt.grid()
# # lo imprime en pantalla
# plt.show()


# # from sklearn.metrics import silhouette_score

# # list_k = list(range(2, 6))

# # lista_coeficientes = pd.DataFrame(columns = ['cant_clusters' , 'coeficiente_silueta'])


# # for n_clusters in list_k:
# #     clusterer = KMeans(n_clusters=n_clusters)
# #     preds = clusterer.fit_predict(scaled_1)
# #     centers = clusterer.cluster_centers_

# #     score = silhouette_score (scaled_1, preds)

# #     # print ("For n_clusters =" + str(n_clusters) + " silhouette score is " + str(score))

# #     lista_coeficientes = lista_coeficientes.append({'cant_clusters' : str(n_clusters), 'coeficiente_silueta' : str(score) }, ignore_index=True)

# # lista_coeficientes.to_csv(r'code\punto5\lista_coeficientes.csv')

# # from yellowbrick.cluster import SilhouetteVisualizer

# # # Genero un modelo con K=3
# # model = KMeans(3, random_state=0)

# # # Ploteo el gráfico de silueta
# # visualizer = SilhouetteVisualizer(model, colors='yellowbrick')    # Instancio el visualizador
# # visualizer.fit(scaled_1)
# # visualizer.show()   


from scipy.cluster.hierarchy import dendrogram, linkage

H = linkage(scaled_1, 'single')

from scipy.spatial.distance import pdist, squareform

squareform(pdist(scaled_1))

max_d = 7.08
plt.figure(figsize=(25, 10))
plt.title('Dendrograma')
plt.xlabel('Observaciones')
plt.ylabel('Distancia')
dendrogram(
    H, truncate_mode='lastp',
    p=150, leaf_rotation=90.,
    leaf_font_size=8.,
)
plt.axhline(y=max_d, c='k')
plt.show()