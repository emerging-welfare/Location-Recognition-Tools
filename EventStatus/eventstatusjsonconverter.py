import os
import sys
import pickle as pk
import json
args = sys.argv
path = 'EventStatus/data/English/annotated-texts'
outname = "eventstatus_eng"
if len(args)> 1 :
    path = args[1]
if len(args)> 2:
    outname = args[2]
filelist = []
for filename in os.listdir(path):
    filelist.append(filename)
def initializedocdict(path,docname):
    f1 = open(os.path.join(path,docname)).readlines()
    filedict = {"doc_name " : docname , "title" : "" , "metadata" : "" ,"text": "",
                "chunk_inds": [], "chunks" : [] , "phrase_level_tags" : [] ,
                "keyword_inds" : [] , "phrase_level_votes": [],
                "keywords": [],"sentence_level_tags": [] ,  
                "sentence_level_votes": []}
    filedict["title"] = f1[1].strip("\n")
    filedict["metadata"] = f1[3]
    chunkinds = [(0,4)]
    text = ""
    ind1 = 0
    chunk1 = (0,0)
    for i,line in enumerate(f1):  
        if "<CHUNK>" in line:
            ind1 = i+1
        elif "</CHUNK>" in line:
            chunkinds.append((ind1,i))
    for x in range(1,len(chunkinds)):
        for i in range(chunkinds[x-1][1]+1,chunkinds[x][0]-1):
            text+= f1[i].strip("\n")
        chunk = ""
        for x in range(chunkinds[x][0],chunkinds[x][1]+1):
            chunk+=f1[x].strip("\n")
        #print(chunk)
        chunkdic = chunktojson(chunk)
        #print(chunkdic)
        text+=chunkdic["chunks"]
        for key in chunkdic:
            filedict[key].append(chunkdic[key])
    for j in range(chunkinds[-1][1]+1,len(f1)):
        text+=f1[j].strip("\n")
    filedict["text"] = text
    for chunk in filedict["chunks"]:
        ind1 = filedict["text"].find(chunk)
        filedict["chunk_inds"].append((ind1,ind1+len(chunk)))
    return filedict

def chunktojson(chunk):
    chunks = chunk.split()
    chunkdict = {}
    text = ""
    phraseind= -1
    for i in range(len(chunks)):
        if chunks[i] == "|||":
            phraseind = i
            break
        else:
            text+=chunks[i]+" "
    chunkdict["keywords"] = chunks[phraseind-1]
    chunkdict["keyword_inds"] = phraseind -1
    chunkdict["phrase_level_tags"] = chunks[phraseind+1]
    chunkdict["phrase_level_votes"] = chunks[phraseind+2]
    for i in range(phraseind+3, len(chunks)-5):
        text+=chunks[i]+" "
    text+=chunks[-5]
    chunkdict["chunks"] = text
    chunkdict["sentence_level_tags"] = chunks[-2]
    chunkdict["sentence_level_votes"] = chunks[-1]
    return chunkdict

def jsonconvert(path,filelist):
    phrasetags = ["NA","PA", "OG" , "FP" , "FT" , "FM" ]
    sentencelevel = ["NO","CU"]
    cunodocs = []
    bothdocs = []
    cunojson = []
    bothjson = []
    phrcounts = {key : 0 for key in phrasetags}
    sentcounts = {key : 0 for key in sentencelevel}
    print(filelist[10])
    for filename in filelist : 
        if ".txt" in filename:
            file2 = open(path+"/"+filename).readlines()
            #print(file2[0])
            if "CUNO_PHASE_ONLY"  in file2[0]:
                cunodocs.append(filename)
            else:
                bothdocs.append(filename)
    for cunodoc in cunodocs:
        d1 = initializedocdict(path,cunodoc)
        cunojson.append(d1)
    for bothdoc in bothdocs:
        d2 = initializedocdict(path,bothdoc)
        bothjson.append(d2)
    print(len(cunodocs))
    print(len(bothdocs))
    return cunojson,bothjson

cunojson , bothjson = jsonconvert(path,filelist)


file1 = open(outname+"_cuno.pickle","wb")
pk.dump(cunojson,file1)
file1.close()
file1 = open(outname+"_cuno.json","wb")
json.dump(cunojson,file1)
file1.close()
file2 = open(outname+"_both.pickle","wb")
pk.dump(bothjson,file2)
file2.close()
file2 = open(outname+"_both.json","wb")
json.dump(bothjson,file2)
file2.close()
