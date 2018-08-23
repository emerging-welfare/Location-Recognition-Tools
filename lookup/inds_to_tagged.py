import sys

args=sys.argv



def inds_to_lines(indf,corp):
	ind1=open(indf).readlines()
	corp1=open(corp).read()
	inds=[int(x.split()[0]) for x in ind1]
	ends=[int(x.split()[1]) for x in ind1]
	lens=[len(x.split()) for x in ind1]
	charindex=0
	linecount=0
	lines=[]
	for i1 in range(len(inds)):
		i=inds[i1]
		len1=lens[i1]
		if i < charindex:
			charindex=0
			linecount=0
		a=corp1[charindex:i].count("\n")
		linecount+=a
		for y in range(len1-2):
			lines.append(linecount)
			linecount+=1
		charindex=(ends[i1]+1)
	return lines



def taglines(corp,lines,out):
	corp1=open(corp).readlines()
	out1=open(out,"w")
	for i in range(len(corp1)):
		if i in lines:
			out1.write(corp1[i][:-1]+" LOC\n")
		else:
			if len (corp1[i])>2:
				out1.write(corp1[i][:-1]+" O\n")
			else:
				out1.write("\n")
	out1.close()


if args[1]=="-h":
	print('inds_to_tagged.py lookupf corfnotags corpfwtags outfile')
else:
	lookupf=args[1]
	corpfnotags=args[2]
	corpfwtags=args[3]
	taggedcorp=args[4]
	lines1=inds_to_lines(lookupf,corpfnotags)
	taglines(corpfwtags,lines1,taggedcorp)







