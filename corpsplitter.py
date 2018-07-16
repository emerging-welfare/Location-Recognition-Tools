####split corpus by DOCSTART
## 0.8 train
## 0.1 val
## 0.1 test


import sys
import argparse
import random
from argparse import RawTextHelpFormatter

def splitcorpus(corpus,train_size,test_size):
	corp=open(corpus).readlines()
	corp1=open(corpus).read()
	train=open("train.txt","w")
	valid=open("valid.txt","w")
	test=open("test.txt","w")
	i=0
	c=1 ## count number of DOCSTART
	total=corp1.count("DOCSTART")
	trsize=total*train_size
	testsize=total*test_size
	valsize=total*(1-train_size-test_size)
	inds=[]
	for i in range(len(corp)):
		if corp[i].find("DOCSTART")!=-1:
			#print(i)
			inds.append(i)
	random.seed(3)
	random.shuffle(inds)
	ind1=0
	for x in range(int(trsize)):
		ind=inds[ind1]
		line1=corp[ind]
		train.write(line1)
		ind+=1
		while "DOCSTART" not in corp[ind] and ind < len(corp)-1:
			train.write(corp[ind])
			ind+=1
		ind1+=1
	for x in range(int(testsize)):
		ind=inds[ind1]
		line1=corp[ind]
		test.write(line1)
		ind+=1
		while "DOCSTART" not in corp[ind] and ind < len(corp)-1:
			train.write(corp[ind])
			ind+=1
		ind1+=1
	for x in range(int(valsize)):
			ind=inds[ind1]
			line1=corp[ind]
			valid.write(line1)
			ind+=1
			while "DOCSTART" not in corp[ind] and ind < len(corp)-1:
				valid.write(corp[ind])
				ind+=1
			ind1+=1
def argparser(args1):
	parser = argparse.ArgumentParser(description='''NeuroNER CLI''', formatter_class=RawTextHelpFormatter)
	parser.add_argument('--corpus_name',required=False)
	parser.add_argument('--train_size', required=False)
	parser.add_argument('--valid_size', required=False)
	parser.add_argument('--test_size',required=False)
	arguments = parser.parse_args(args=args1)
	return arguments
filename="ACEconllformat"
train_size=0.8
test_size=0.2
valid_size=0
args=sys.argv
argparsed= vars(argparser(args[1:]))
filename=argparsed["corpus_name"]
train_size=float(argparsed["train_size"])
if argparsed["valid_size"] != None:
	valid_size=float(argparsed["valid_size"])
test_size=float(argparsed["test_size"])
if train_size +test_size != 1:
	valid_size = 1-test_size - train_size
print("filename: " + filename)
print("train validation test sizes : " + str(train_size)+" " + str(valid_size) + " "+ str(test_size))
splitcorpus(filename,train_size,test_size) 

