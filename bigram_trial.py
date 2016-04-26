import math
#import nltk
# function for adding start and stop symbol
# * corresponds to start symbol and # corresponds to stop symbol
def modify_data(data):
    fin = open(data)
    fout= open("new_data.txt","w")
    for line in fin:
        words= line.split()
        str= words[0]+' * '
        fout.write(str)

        for i in range (1,len(words)):
            fout.write( words[i]+' ')

        fout.write(' # ')
        fout.write("\n")
    return
# creates separate documents for positive and negative sentences
def create_doc(data):
    pos_write = open("positive_new.txt","w")
    neg_write= open("negative_new.txt","w")

    fo= open(data)
    global class_p
    class_p=0
    global class_n
    class_n=0
    for line in fo:
        words = line.split()

        if words[0]=='+':
            pos_write.write(line)
            class_p=class_p+1


        elif words[0]=='-':
            neg_write.write(line)
            class_n= class_n+1
    pos_write.close()
    neg_write.close()

    return
# gives all possible bigrams in a given document
def create_bigram(data):
    f1= open("bigram_data.txt","w")
    f2=open(data)
    for line in f2:
        words = line.split()
        for i in range(1,len(words)-1):
            f1.write(words[i]+words[i+1])
            f1.write("\n")
    return


#function for creating vocabulary with both unigram and bigram features
def create_vocab(data):
    global vocab
    vocab=[]
    temp_1= open(data)
    megadoc=""
    for line in temp_1:
        check= line.split()
        line= line.replace(check[0],"")
        megadoc = megadoc+line
    words = megadoc.split()

    for i in range(0,len(words)):
        if words[i] not in vocab:


            freq= words.count(words[i])
            if freq>1:

                vocab.append(words[i])
    modify_data(data)
    create_bigram("new_data.txt")
    temp = open("bigram_data.txt")
    megadoc = ""
    for line in temp:

        megadoc= megadoc+ line
    words = megadoc.split()

    for i in range(0,len(words)):

        if words[i] not in vocab:

           freq= words.count(words[i])

           if freq>3:
               vocab.append(words[i])
    return vocab



# for calculating the frequencies of words in + class
def pos_frequency(data):
    global total_pos
    total_pos=0
    global pos_words
    pos_words=[]
    global pos_count
    pos_count=[]
    pos_write = open(data)
    megadoc =""
    for line in pos_write:
        check=line.split()
        line= line.replace(check[0],"")
        megadoc = megadoc+line
    words = megadoc.split()
    total_pos = total_pos+len(words)

    for i in range(0,len(words)):
        if words[i] in vocab:
            if words[i] not in pos_words:

               pos_words.append(words[i])
               x= words.count(words[i])
               pos_count.append(x)
    modify_data(data)
    create_bigram("new_data.txt")
    pos_write = open("bigram_data.txt")
    megadoc = ""
    for line in pos_write:
        megadoc= megadoc+ line
    words = megadoc.split()
    total_pos= total_pos+len(words)



    for i in range(0,len(words)):
        if words[i] in vocab:
            if words[i] not in pos_words:

                pos_words.append(words[i])
                x= words.count(words[i])
                pos_count.append(x)

    pos_write=open("new_data.txt")

    temp_array = []
    for line in pos_write:
        check= line.split()
        line= line.replace(check[0],"")
        words = line.split()
        for i in range(1,len(words)):
            if words[i-1]+words[i] in pos_words:
                if words[i-1]+words[i] not in temp_array:
                    temp_array.append(words[i-1]+words[i])
                    if words[i-1] in pos_words:
                      index_u= pos_words.index(words[i-1])
                      count_u = pos_count[index_u]
                      index_b= pos_words.index(words[i-1]+words[i])
                      count_b= pos_count[index_b]
                      pos_count[index_u]= count_u-count_b
                      total_pos = total_pos-count_b

                    if words[i] in pos_words:
                      index_u= pos_words.index(words[i])
                      count_u = pos_count[index_u]
                      index_b= pos_words.index(words[i-1]+words[i])
                      count_b= pos_count[index_b]
                      pos_count[index_u]= count_u-count_b
                      total_pos = total_pos-count_b


    pos_write.close()
    return
# for calculating the frequencies of words in - class
def neg_frequency(data):
    global neg_words
    neg_words=[]
    global neg_count
    neg_count=[]
    global total_neg
    total_neg=0
    neg_write = open(data)
    megadoc = ""
    for line in neg_write:
        check = line.split()
        line= line.replace(check[0],"")
        megadoc= megadoc+ line
    words = megadoc.split()
    total_neg= total_neg+ len(words)

    for i in range(0,len(words)):
        if words[i] in vocab:
            if words[i] not in neg_words:

                neg_words.append(words[i])
                x= words.count(words[i])
                neg_count.append(x)

    modify_data(data)
    create_bigram("new_data.txt")

    neg_write = open("bigram_data.txt")
    megadoc = ""
    for line in neg_write:
        megadoc= megadoc+ line
    words = megadoc.split()
    total_neg= total_neg+len(words)

    for i in range(0,len(words)):
        if words[i] in vocab:
            if words[i] not in neg_words:

                neg_words.append(words[i])
                x= words.count(words[i])
                neg_count.append(x)

    neg_write=open("new_data.txt")
    temp_array=[]
    for line in neg_write:
     check= line.split()
     line= line.replace(check[0],"")
     words = line.split()
     for i in range(1,len(words)):
        if words[i-1]+words[i] in neg_words:
            if words[i-1]+words[i] not in temp_array:
                temp_array.append(words[i-1]+words[i])
                if words[i-1] in neg_words:

                    index_u= neg_words.index(words[i-1])
                    count_u = neg_count[index_u]
                    index_b= neg_words.index(words[i-1]+words[i])
                    count_b= neg_count[index_b]
                    neg_count[index_u]= count_u-count_b
                    total_neg = total_neg-count_b
                if words[i] in neg_words:
                    index_u= neg_words.index(words[i])
                    count_u = neg_count[index_u]
                    index_b= neg_words.index(words[i-1]+words[i])
                    count_b= neg_count[index_b]
                    neg_count[index_u]= count_u-count_b
                    total_neg = total_neg-count_b





    neg_write.close()
    return
def calc_posprob(word):
    prob_p=0
    prob_1=0
    prob_p = math.log2(class_p/(class_p+class_n))

    not_present =0
    nothing=0
    for i in range(1,len(word)):

        count=0


        if word[i-1]+word[i] in vocab:
            if word[i-1]+word[i] in pos_words:
                index= pos_words.index(word[i-1]+word[i])
                count= pos_count[index]

                not_present=0
        else:
            if not_present==0:
                if word[i-1]=='*':
                    if word[i] in pos_words:
                        index= pos_words.index(word[i])
                        count=pos_count[index]
                    else:
                        count=0
                else :
                    if word[i]=='#':
                      if word[i-1] in pos_words:
                        index= pos_words.index(word[i-1])
                        count=pos_count[index]
                      else:
                        count=0
                    else:
                        if word[i] in pos_words:
                            index= pos_words.index(word[i])
                            count=pos_count[index]
                        else:
                            count=0
                not_present=1
            else:
                if word[i]=='#':
                    nothing=1
                else:
                    if word[i] in pos_words:
                        index= pos_words.index(word[i])
                        count= pos_count[index]

        if nothing:
            count=0
        else:
            if count <0:
                count=0

            prob_1= math.log2((count+1)/(total_pos+len(vocab)))
        prob_p= prob_p+prob_1
    return prob_p




def calc_negprob(sentence):
    prob_n=0
    prob_1=0
    prob_n = math.log2(class_n/(class_p+class_n))
    word=sentence
    nothing =0
    not_present =0;
    for i in range(1,len(word)):
        count=0


        if word[i-1]+word[i] in vocab:
            if word[i-1]+word[i] in neg_words:
                index= neg_words.index(word[i-1]+word[i])
                count= neg_count[index]

                not_present=0
        else:
            if not_present==0:
                if word[i-1]=='*':
                    if word[i] in neg_words:
                        index= neg_words.index(word[i])
                        count=neg_count[index]
                    else:
                        count=0
                else :
                    if word[i]=='#':
                      if word[i-1] in neg_words:
                        index= neg_words.index(word[i-1])
                        count=neg_count[index]
                      else:
                        count=0
                    else:
                        if word[i] in neg_words:
                            index= neg_words.index(word[i])
                            count=neg_count[index]
                        else:
                            count=0
                not_present=1
            else:
                if word[i]=='#':
                    nothing=1
                else:
                    if word[i] in neg_words:
                        index= neg_words.index(word[i])
                        count= neg_count[index]
        if nothing:
            count=0
        else:
            if count<0:
                count=0

            prob_1= math.log2((count+1)/(total_neg+len(vocab)))
        prob_n= prob_n+prob_1
    return prob_n


def multinomial_naive_bayes(data,test):

    create_doc(data)
    create_vocab(data)



    pos_frequency("positive_new.txt")
    neg_frequency("negative_new.txt")


    tp=0
    tn=0
    fp=0
    fn=0
    modify_data(test)
    test_file = open("new_data.txt")
    i=1
    for line in test_file:
        sentence = line.split()

        if sentence[0]=='+':
            original = 1
            sentence.remove('+')
        else:
            original =0
            sentence.remove('-')
        pos_prob = calc_posprob(sentence)
        neg_prob = calc_negprob(sentence)
        if pos_prob>neg_prob:
            detected =1
        else:
            detected =0

        i=i+1
        if original==1 and detected==1:
            tp=tp+1
        elif original ==0 and detected==1:
            fp=fp+1
        elif original ==1 and detected ==0:
            fn=fn+1
        else:
            tn=tn+1
    accuracy = (tn+tp)/(tn+tp+fp+fn)
    #print(accuracy)

    return accuracy
#multinomial_naive_bayes("check.txt","check_neg.txt")



i=0
j=250
avg_accuracy=[]
for p in range(1,11):



    #input_data = open("data_without_stopwords.txt","r")
    input_data=open("dataset_combined.txt","r")
    #input_data = open("new_data.txt","r")
    count_positive=0
    count_negative=0
    train=""
    test=""
    k=0



    for line in input_data:
        if k in range(i,i+25):
            #print(k)
            test +=line
        elif k in range(j,j+25):
            #print(k)
            test +=line
        else:
            train = train+line
        k=k+1


##        #print(line)
##        words=line.split()
##        if words[0]=='+':
##            count_positive +=1
##        elif words[0]=='-':
##            count_negative +=1
##        if words[0]=='+' and count_positive > i and count_positive <= j:
##            test += line
##        elif words[0]=='-' and count_negative > i and count_negative <= j:
##            test += line
##        else:
##            train += line

    input_data.close()

    train_list= open("train.txt","w")
    test_list=open("test.txt","w")

    for l in range(len(train)):
        train_list.write(train[l])
    for l in range(len(test)):
        test_list.write(test[l])
    train_list.close()
    test_list.close()

    accuracy=multinomial_naive_bayes("train.txt","test.txt")
    print(accuracy)
    avg_accuracy.append(accuracy)
    i=i+25
    j=j+25

print( sum(avg_accuracy)/len(avg_accuracy))
