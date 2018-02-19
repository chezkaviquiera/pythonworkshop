countC=0
countG=0
text_file=open("DNA.txt").read()
total=len(text_file)

for i in range (len(text_file)):
    if text_file[i]=="C":
        countC=countC+1.00
    if text_file[i]=="G":
        countG=countG+1.00

print "Total percentage of C+G: ",((countC+countG)/(total))*100
