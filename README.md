#CONTENT

# Implemented Algorithms
* Affinity Propagation (AP)
* Spectral CLustering 
* K-Means

# Evaluation
* F-Measure
* Adjusted Random Index (ARI)

# FIles
* cluster_gs    = Gold standard clusters
* kmeans_result = Clusters predicted by k_meanns  

* evaluate.py = contains evaluation of clustering using F-Measure and ARI
* elbow.py    = Finding number of clusters unsing elbow method
* KMeans.py   = KMeans implementation
* AP.py       = AP implementation
* SpcCl.py    = Spectral Clustering implementation

* pre_preocess.py = Processing Data, stopword removal, stemming, computing tfidf and cosine similarity
* data.txt        = stackoverflow data taken from https://github.com/jacoxu/StackOverflow
