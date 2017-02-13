from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise        import cosine_similarity
from nltk.stem.lancaster             import LancasterStemmer

import scipy
import numpy as np

# stemmer
st = LancasterStemmer()

# Helper function for applying stemming
def stemList(lin):
    lout = list()
    for item in lin:
         lout.append(st.stem(is_ascii(item)))
    return lout

# avid unicode characters
def is_ascii(s):
    if all(ord(c) < 128 for c in s):
        return s
    else:
        return "a"

#stemming: Bring words to their root format
def applyStemming(arg):
   stemmed = list()
   for item in arg:
       stemmed.append(" ".join(stemList(item.split())))
   return stemmed

# whole matrix print mode
np.set_printoptions(threshold=np.inf)


# reads the data from txt file and adds each document to a list
with open('data.txt') as file:
    train_set = list()
    for line in file:
        train_set.append(line.lower())

train_set_stemmed = applyStemming(train_set)

vectorizer = CountVectorizer(stop_words='english')
document_term_matrix = vectorizer.fit_transform(train_set_stemmed)

# vocabulary size
# print len(vectorizer.vocabulary_)

tfidf = TfidfTransformer()
tfidf.fit(document_term_matrix)

# "IDF: ", tfidf.idf_ << inverse document frequency
tf_idf_matrix = tfidf.transform(document_term_matrix)

# Cosine similarity matix which is feed as an input to a
# clustering algorithm
# pairwise_similarity = tf_idf_matrix * tf_idf_matrix.T
co_sim_matrix = cosine_similarity(tf_idf_matrix, tf_idf_matrix)
