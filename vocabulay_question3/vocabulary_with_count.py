
#count the frequemcies of each word in the document and write the unique words into a separate document
start=open('final_refine_doc.txt').read()
wordfreq=[]
sum = 0
wordlist=start.split()
for word in wordlist:
    if (wordlist.count(word) > 1):
        wordfreq.append([word,wordlist.count(word)])



#print ("String\n" + start +"\n")
#print ("List\n" + str(wordlist) + "\n")
#######print ("Frequencies\n" + str(wordfreq) + "\n")
#print ("Pairs\n" + str(zip(wordlist, wordfreq)))
my_list=[]

for item in wordfreq:
    for term in item:
        my_list.append(term)
        break
list1=set(my_list)
#print (my_list)
#print (list1)
out = open('vocablary_count.txt','w')
flag=1
for item in wordfreq:
    for term in item:
        if flag == 1:
            if term in list1:
                out.write("{0}".format(term))
                out.write(" ")
                flag=0
                list1.remove(term)
        else:
            out.write("{0}".format(term))
            out.write("\n")
            flag=1
