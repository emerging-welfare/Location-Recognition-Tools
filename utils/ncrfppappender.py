import sys

from optparse import OptionParser

def sharprem(corpn,outn):
    l1=[]
    out=open(outn,"w")
    corp=open(corpn).readlines()
    for line in corp:
        if line[0]!="#":
            l1.append(line)
            out.write(line)
    out.close()
    return l1
def appendpreds(corpn,predn,outn):
    out=open(outn,"w")
    corp=open(corpn).readlines()
    pred=open(predn).readlines()
    for line1,line2 in zip(corp,pred):
        if len(line1)>2:
            ls=line2.split()
            out.write(line1[:-1]+" ")
            out.write(ls[-1]+"\n")
        else:
            out.write(line1)
    out.close()

if __name__=="__main__":
    parser=OptionParser()
    parser.add_option("--goldfile", dest="gold_file", help="Path to gold labeled file", metavar="FILE", default="N/A")
    parser.add_option("--predfile", dest="pred_file", help="Path to prediction file", metavar="FILE", default="N/A")
    parser.add_option("--outfile", dest="out_file", help="Path to prediction file", metavar="FILE", default="output)
    inter="sharpremovedpredfile"
    (options, args) = parser.parse_args()
    goldf = options.gold_file
    predf = options.pred_file
    outf  = options.out_file
    print("Produced intermediate file named :  %s" %inter)
    sharprem(predf,inter)
    appendpreds(goldf,inter,outf)
