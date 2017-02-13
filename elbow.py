import matplotlib.pyplot as plt
from pre_process import *
from sklearn.cluster import KMeans
import numpy as np

# elbow method: finding number of clusters

# distortions = []
# for i in range(1, 20):
#     km = KMeans(n_clusters = i, init = 'k-means++', n_init = 20, max_iter = 300, random_state = 0)
#     km.fit(co_sim_matrix)
#     distortions.append(km.inertia_)
#
# plt.plot(range(1,20), distortions, marker='o')
# plt.xlabel('Number of clusters')
# plt.ylabel('Distortion')
# plt.show()
#
#
# ambiguos curve
x = list()
for i in range (1, 20):
    x.append(1000/i)

plt.plot(range(1, 20), x, marker = 'o')
plt.show()
