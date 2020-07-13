gloveFile = "glove.6B.100d.txt"
import numpy as np
import re
from nltk.corpus import stopwords
import pandas as pd
import pickle


class demo:

   
    def __init__(self):
        with open('out.pickle', 'rb') as f:
            self.model = pickle.load(f)

    def loadGloveModel(self,gloveFile):
        print ("Loading Glove Model")
        with open(gloveFile, encoding="utf8" ) as f:
            content = f.readlines()
        model = {}
        for line in content:
            splitLine = line.split()
            word = splitLine[0]
            embedding = np.array([float(val) for val in splitLine[1:]])
            model[word] = embedding
        print ("Done.",len(model)," words loaded!")
        return model

    def preprocess(self,raw_text):

        # keep only words
        letters_only_text = re.sub("[^a-zA-Z]", " ", raw_text)

        # convert to lower case and split 
        words = letters_only_text.lower().split()

        # remove stopwords
        stopword_set = set(stopwords.words("english"))
        cleaned_words = list(set([w for w in words if w not in stopword_set]))

        return cleaned_words

    def cosine_distance_wordembedding_method(self,s1, s2):
        import scipy
        vector_1 = np.mean([self.model[word] for word in self.preprocess(s1)],axis=0)
        vector_2 = np.mean([self.model[word] for word in self.preprocess(s2)],axis=0)
        cosine = scipy.spatial.distance.cosine(vector_1, vector_2)
        print('Word Embedding method with a cosine distance asses that our two sentences are similar to',round((1-cosine)*100,2),'%')
        return round((1-cosine)*100,2)



