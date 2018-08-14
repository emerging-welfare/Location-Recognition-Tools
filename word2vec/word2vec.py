from gensim import corpora, models, similarities
from gensim.models import Word2Vec
from gensim.test.utils import common_texts, get_tmpfile
import gzip
import numpy as np
import gensim 
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import sys

args=sys.argv

filename=args[1]
size1=100
window1=5
min1=2
epc1=50
modelname="word2vec.model"
vecdictname="vecdict"


sents=open(filename).readlines()
corp=[]
for sent in sents:
    corp.append(gensim.utils.simple_preprocess (sent))
model = Word2Vec(corp,size=size1,window=window1,min_count=min1,workers=1)

model.train(corp, total_examples=len(corp), epochs=epc1)

model.save(modelname)
wordvecs=model.wv
worddic={}
for word in wordvecs.vocab:
    worddic[word]=wordvecs[word]

def saveword2vecdic(dic1,outn):
    out=open(outn,"w")
    for key, val in dic1.items():
        out.write(key + "\t")
        for v in val:
            out.write(str(v)+" ")
        out.write("\n")
    out.close()

saveword2vecdic(worddic,vecdictname)

print("Word2vec model file: %s" %modelname)
print("Dictionay name: %s" %vecdictname)
