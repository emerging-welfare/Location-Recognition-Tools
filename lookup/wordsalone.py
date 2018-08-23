import sys
as1=sys.argv
fname=as1[1]
out=as1[2]
corp=open(fname).readlines()
outf=open(out,"w")
for l in corp:
    if len(l)>1:
        outf.write(l.split()[0]+"\n")
    else:
        outf.write("\n")
outf.close()
