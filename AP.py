from sklearn.cluster import AffinityPropagation
from pre_process import *

#############  AffinityPropagation ##########################
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs

af = AffinityPropagation(damping = 0.5, preference=-50).fit(co_sim_matrix)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_
n_clusters_ = len(cluster_centers_indices)

print "Affinity computed ______> "

cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_
print "num cluusters: ", len(labels)
n_clusters_ = len(cluster_centers_indices)

a_dict_ = {}
af_dict = map(lambda k, v: a_dict_.update({k: v}), train_set,labels)

for item in a_dict_.items():
    print item
