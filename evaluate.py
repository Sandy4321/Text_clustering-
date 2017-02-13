from pre_process import *
from sklearn     import metrics
import numpy as np

with open('true_labels.txt') as file:
    labels = list()
    for line in file:
        labels.append(int(line))

labels_np = np.array(labels) - 1
labels_np_lst = labels_np.tolist()




clusters  = [[] for i in range(0, 20)]


for j in range(1, 21):
    for i in range(0,20000):
        if labels[i] == j:
            clusters[j-1].append(train_set[i])



clusters_kmean = [[] for i in range(0, 20)]
for i in range (0, 20):
    with open('kmeans_result/'+str(i)+'.txt') as file:
        for line in file:
            clusters_kmean[i].append(line)


# COMPPUTE CORRESPONDENCE MATRIX

# returns length of intersection of two lists
def intersect(lst1, lst2):
    set2  = set(lst2)
    res   = [val for val in lst1 if val in set2]
    return len(res)


mat = np.zeros(shape=(20, 20))

for i in range(0, 20):
    for j in range(0, 20):
        mat[i, j] = intersect(clusters[i], clusters_kmean[j])

#
# max_elem_indicies = mat.argmax(axis=1)
# print max_elem_indicies
#
# lst = list()
#
# for i in range(20):
#     for j in range(20):
#         if i != j:
#             if max_elem_indicies[i] == max_elem_indicies[j]:
#                lst.append(max_elem_indicies[i])
#
# lst1 = list(set(lst))
#
# # change all to zero except max element
#
# for item in lst1:
#     k =  max(mat[:, item])
#     for i in range(20):
#         if mat[i][item] != k:
#             mat[i][item] = 0
#

correspondence_vect = [18, 1, 13, 12, 9, 8, 11, 7, 10, 5,  6,  3, 15, 0,  14, 16, 19,  4, 17,  2]


with open ('k_means_labels.txt') as file:
    km_labels = list()
    for line in file:
        km_labels.append(correspondence_vect.index(int(line[:-1])))


# Evaluation using Adjusted Random Index
# labels_np_lst = true labels
# km_labels     = Predicted labels
performance_RI = metrics.adjusted_rand_score(labels_np_lst, km_labels)



print performance_RI

from sklearn.metrics import precision_recall_fscore_support
(p, r, f, k) = precision_recall_fscore_support(labels_np_lst, km_labels, average='macro')



print f
