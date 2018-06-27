from lxml import etree
import xml.etree.ElementTree as ET
import sys
def xmltointernam(xmlfile,rawfile,entypes):
    tree = ET.parse(xmlfile)
    treeraw=etree.parse(rawfile)
    rootraw=treeraw.getroot()
    root = tree.getroot()
    names=[]
    inds=[]
    typel=[]
    for doc in root.findall('document'):
        for entity in doc.findall('entity'):
            type1= entity.get('TYPE')
            if type1 in entypes:
                mentions=entity.findall('entity_mention')
                for ment in mentions:
                    mentype1=ment.get("TYPE")
                    if mentype1=="NAM":
                        extent1=ment.find("head")
                        charseq1=extent1.find("charseq")
                        names.append(charseq1.text)
                        inds.append(int(charseq1.get('START'))-1)
                        typel.append(type1)
    body=rootraw.find("BODY")
    tex=[x for x in rootraw.itertext()]
    tex[0]=tex[0][1:]
    text1=""
    for t in tex:
        text1=text1+t
    text1=text1.replace("\n"," ")
    return text1, names, inds ,typel

##given char start indexes 
##returns the corresponding token index of the given token
def chartotokinds(text1,inds):
    tokids=[]
    for i in range(len(inds)):
        str1=text1[:inds[i]-1]
        str1s=str1.split()
        tokids.append(len(str1s))
    return tokids

## for multi-word entities
## add the indexes of the non-starting tokens
## in order to tag them as well 
def expandtokinds(tokinds,toks,typel):
    exptokinds=[]
    exptypel=[]
    for i in range(len(tokinds)):
        len1=len(toks[i].split())
        for l in range(len1):
            exptokinds.append(tokinds[i]+l)
            exptypel.append(typel[i])
    return exptokinds,exptypel




## given as input the .apf.xml and .sgm files 
## outputs the document in wapiti format
## by only considering the entity types in the 'types' list
## if outtyp parameter is 0 then all entities are tagged as '1' and 0 o/w
## else every entity is tagged with its own type
def xmltowapiti(xmlfile,rawfile,types,outfile,outtyp):
    text1, ents,inds, typel = xmltointernam(xmlfile,rawfile,types)
    tokinds=chartotokinds(text1,inds)
    exptokinds,exptypel=expandtokinds(tokinds,ents,typel)
    out=open(outfile,"a")
    ts=text1.split()
    for i in range(len(ts)):
        out.write(ts[i]+" ")
        ind1= findind(exptokinds,i)
        if ind1!=-1:
            if outtyp==0:
                out.write("1\n")
            else:
                out.write(exptypel[ind1]+"\n")
        else:
            out.write("O \n")


##in order this function to work
## the address of the file.tbl file must be givene
## returns the names of the files in the adj folders for English
def filenamelist(base,filelistfile):
    filenames=open(filelistfile).readlines()
    englishnames=[]
    for name in filenames:
        if "data/English" in name and ".apf.xml" in name and ".score" not in name and "adj" in name:
            englishnames.append(base+name[:name.find(".apf.xml")])
    return englishnames




##converts & in documents to &amp;
## this step is required for the .sgm files
## output files have the suffix .sgm1
def andsignupdate(filenames):
    for name in filenames:
        name1=name+".sgm"
        read1=open(name1).read()
        write1=open(name1+"1","w")
        for x in read1:
            if x=="&":
                write1.write("&amp;")
            else:
                write1.write(x)




##for all English documents 
## create corpus in wapiti format
def toWapitiCorpus(base,filenames,outfilename,tagver,tagtypes):
    count=0
    for doc in filenames:
        name=doc
        #print(doc)
        count+=1
        xmltowapiti(name+".apf.xml",name+".sgm1",tagtypes,outfilename,tagver)
    print("%d files are converted" %count)

##returns the position of a given value in a list
def findind(l1,ind1):
    for i in range(len(l1)):
        if ind1==l1[i]:
            return i
    return -1

def ACEtoTokenPerLine(base,filelistfile,outfilename,tagtypes,tagver):
    filenames=filenamelist(base,filelistfile)
    andsignupdate(filenames)
    toWapitiCorpus(base,filenames,outfilename,tagver,tagtypes)

def defaultaddr():
	base1="ACE/aceCorp/"
	filelistfile1="ACE/aceCorp/docs/file.tbl"
	outfilename1="acetowapCorpus2"
	tagtypes1=["ORG","LOC","GPE","PER"]
	tagver1=0

def assignvars(args):
	tagtypes1=[]
	base1=args[1]
	filelistfile1=args[2]
	outfilename1=args[3]
	for x in args[4:-1]:
		tagtypes1.append(x)
	tagver1=args[-1]


base1="ACE/aceCorp/"
filelistfile1="ACE/aceCorp/docs/file.tbl"
outfilename1="acetotokenCorpus"
tagtypes1=["ORG","LOC","GPE"]
tagver1=0


args=sys.argv
if len(args)>1:
	if args[1]=="-h":
		print("python3 aceconv.py base filelistfile outfilename tagtypes tagver")
		print("python3 aceconv.py def  | for default mode")
	elif args[1]=="def":
		print("running on default mode")
		print("base: ACE/aceCorp/")
		print("filelist address: ACE/aceCorp/docs/file.tbl")
		print("output file name: acetotokenCorpus")
		print("Tag types: ORG LOC GPE")
		print("Tagging version: binary")
		ACEtoTokenPerLine(base1,filelistfile1,outfilename1,tagtypes1,tagver1)
	else:
		tagtypes1=[]
		base1=args[1]
		filelistfile1=args[2]
		outfilename1=args[3]
		for x in args[4:-1]:
			tagtypes1.append(x)
		tagver1=args[-1]
		ACEtoTokenPerLine(base1,filelistfile1,outfilename1,tagtypes1,tagver1)








