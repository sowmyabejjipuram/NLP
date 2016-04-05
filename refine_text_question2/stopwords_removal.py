#program to remove stopwords

f1= open('refine_doc.txt')
line1=f1.readline()      # original file
f2 = open('stop_words.txt').read()
        #file having stop words to be removed
out = open('final_refine_doc.txt','w')             #result file
while line1:
    for word1 in line1.split():
        for word2 in f2.split():
            flag=1
            if word1 == word2 :
                flag=0
                break
            else:
                continue

        if flag == 1:
            out.write(word1)
            out.write(" ")
    out.write("\n")
    line1=f1.readline()
