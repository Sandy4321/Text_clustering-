from pre_process import *
from sklearn.cluster import KMeans


def runKMeans(num_clusters):
     kmeans_result = KMeans(n_clusters=num_clusters, init='k-means++').fit_predict(co_sim_matrix)
     return kmeans_result

"""
   n_clusters = The number of clusters
   max_iter   = Maximum number of iterations of the k-means algorithm for singke run
   n-init     = The number of time the k-means algorithm will be run with different centroid seeds
   init {'k-means++', 'random'  or ndarray} = method for initialization,
        'k-means++' - selects initial cluster centers for k-mean clustering in a smart way
"""
kmeans_result = runKMeans(20)

for item in kmeans_result:
    print item

a_dict_ = {}
k_means_dict = map(lambda k, v: a_dict_.update({k: v}), train_set, kmeans_result)

for j in range(0, 20):
    with open('kmeans_result/'+str(j)+'.txt', 'a') as clusters:
        for i in range(0,20000):
            if kmeans_result[i] == j:
                clusters.write(train_set[i])
