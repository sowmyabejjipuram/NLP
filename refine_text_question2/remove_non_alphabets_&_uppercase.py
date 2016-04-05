import re
#import nltk.corpus
string = open ("dataset_combined.txt")
star=open ("refine_doc.txt",'w')
line=string.readline()
while line:
    new_str=re.sub('[^A-Z a-z]+', '', line)   #removing the non-alphabetic characters
    star.write(new_str.lower())
    star.write("\n")
    line=string.readline()
