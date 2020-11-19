import pandas as pd 

# Lee el archivo
df_data_raw = pd.read_csv(r"code\punto4\trigo.csv") 
# Preview the first 5 lines of the loaded data 
# print(df_data_raw.head())

from sklearn.preprocessing import scale, MinMaxScaler

# scale
scaled_1 = scale(df_data_raw)

from sklearn.cluster import KMeans

# Por defecto usa la distancia euclidea
km = KMeans(
    n_clusters=3, init='random',
    n_init=20, random_state=0
)

y_km = km.fit_predict(scaled_1)

# print(y_km)

# print(km.cluster_centers_)

# print(scaled_1)

# df = pd.DataFrame(km.cluster_centers_)   
# df.to_csv(r'code\punto4\centroides.csv')

df_y_km = pd.DataFrame(y_km,columns=['id_cluster'])   
df_y_km.to_csv(r'code\punto4\y_km.csv')

df_result = pd.merge(df_data_raw,df_y_km,how="inner",left_index=True,right_index=True)
df_result.to_csv(r'code\punto4\merge.csv')

df_cluster_0 = df_result.loc[df_result.loc[:,'id_cluster'] == 0]
df_cluster_0.to_csv(r'code\punto4\df_cluster_0.csv')

df_cluster_1 = df_result.loc[df_result.loc[:,'id_cluster'] == 1]
df_cluster_1.to_csv(r'code\punto4\df_cluster_1.csv')

df_cluster_2 = df_result.loc[df_result.loc[:,'id_cluster'] == 2]
df_cluster_2.to_csv(r'code\punto4\df_cluster_2.csv')

# df = pd.DataFrame(y_km)   
# df.to_csv(r'code\punto4\y_km.csv')

# import matplotlib.pyplot as plt

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
# #scatter del tercer cluster
# plt.scatter(
#     scaled_1[y_km == 2, 0], scaled_1[y_km == 2, 1],
#     s=50, c='lightblue',
#     marker='v', edgecolor='black',
#     label='cluster 3'
# )
# #scatter del los centroides
# plt.scatter(
#     km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
#     s=250, marker='*',
#     c='red', edgecolor='black',
#     label='centroides'
# )
#le pongo la leyenda
# plt.legend(scatterpoints=1)
# #hace una grilla en el grafico
# plt.grid()
# #lo imprime en pantalla
# plt.show()

# from sklearn.metrics import silhouette_score

# list_k = list(range(2, 7))

# for n_clusters in list_k:
#     clusterer = KMeans(n_clusters=n_clusters)
#     preds = clusterer.fit_predict(scaled_1)
#     centers = clusterer.cluster_centers_

#     score = silhouette_score (scaled_1, preds)
#     print ("For n_clusters =" + str(n_clusters) + " silhouette score is " + str(score))

# from scipy.cluster.hierarchy import dendrogram, linkage

# H = linkage(scaled_1, 'single')


# from scipy.spatial.distance import pdist, squareform

# squareform(pdist(scaled_1))

# max_d = 7.08
# plt.figure(figsize=(25, 10))
# plt.title('Dendrograma')
# plt.xlabel('Observaciones')
# plt.ylabel('Distancia')
# dendrogram(
#     H, truncate_mode='lastp',
#     p=150, leaf_rotation=90.,
#     leaf_font_size=8.,
# )
# plt.axhline(y=max_d, c='k')
# plt.show()

# sse = []
# list_k = list(range(1, 10))

# for k in list_k:
#     km = KMeans(n_clusters=k)
#     km.fit(scaled_1)
#     sse.append(km.inertia_)

# Grafico el SSE por K
# plt.figure(figsize=(6, 6))
# plt.plot(list_k, sse, '-o')
# plt.xlabel(r'Cantidad de clusters *k*')
# plt.ylabel('SSE')
# plt.show()


# from sklearn.metrics import silhouette_score

# list_k = list(range(2, 5))

# for n_clusters in list_k:
#     clusterer = KMeans(n_clusters=n_clusters)
#     preds = clusterer.fit_predict(scaled_1)
#     centers = clusterer.cluster_centers_

#     score = silhouette_score (scaled_1, preds)
#     print ("For n_clusters =" + str(n_clusters) + " silhouette score is " + str(score))

# from yellowbrick.cluster import SilhouetteVisualizer

# # Genero un modelo con K=3
# model = KMeans(3, random_state=0)

# # Ploteo el gráfico de silueta
# visualizer = SilhouetteVisualizer(model, colors='yellowbrick')    # Instancio el visualizador
# visualizer.fit(scaled_1)
# visualizer.show()    