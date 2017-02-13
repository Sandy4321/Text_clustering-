from pre_process import *
from sklearn.cluster import SpectralClustering

################ Spectral clustering #############################
specCl_result = SpectralClustering(20).fit_predict(co_sim_matrix)

a_dict = {}
junk = map(lambda k, v: a_dict.update({k: v}), train_set, specCl_result)

for item in a_dict.items():
    print item
