import sys 

args=sys.argv


def corptodic(filen):
    file2=open(filen).readlines()
    f1dict={}
    for line1 in file2:
        ls=line1.split()
        vals=''
        for i in range(1,len(ls)):
            vals+=ls[i]+"\t"
        f1dict[ls[0]]=vals
    return f1dict

def setdiff(f1,f2):
	f1dict=corptodic(f1)
	f2dict=corptodic(f2)
	a=list(set(f1dict.keys())-set(f2dict.keys()))
	fark=open("fark","w")
	for x in a:
		fark.write(x+" "+f1dict[x]+"\n")
	fark.close()
	union=open("union","w")
	for key1 in f2dict.keys():
		union.write(key1+" "+ f2dict[key1]+"\n")
	for x in a:
		union.write(x+" "+f1dict[x]+"\n")
	union.close()


setdiff(args[1],args[2])

