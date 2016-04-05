import math
#from unigram_training import multinomial_naive_bayes

pos_count_sep=0;
neg_count_sep=0;
def separation(data):
    positive = open("positive_part.txt","w")
    negative= open("negative_part.txt","w")
    global pos_count_sep
    global neg_count_sep
    f1= open(data)
    for line in f1:
        words = line.split()

        if words[0]=='+':
            positive.write(line)
            pos_count_sep=pos_count_sep+1

        elif words[0]=='-':
            negative.write(line)
            neg_count_sep=neg_count_sep+1

    positive.close()
    negative.close()

    return

#count the frequemcies of each word in the document and write the unique words into a separate document
def vocabulary(data1,data2):
    start=open(data1).read()

    wordfreq=[]
    sum = 0
    wordlist=start.split()
    for word in wordlist:
        if (wordlist.count(word) > 1):
            wordfreq.append([word,wordlist.count(word)])

    my_list=[]

    for item in wordfreq:
        for term in item:
            my_list.append(term)
            break
    list1=set(my_list)

    out = open(data2,'w')
    flag=1
    for item in wordfreq:
        for term in item:
            if flag == 1:
                if term in list1 and (term != '+' and term != '-'):
                    #print ("{0}".format(term))
                    out.write("{0}".format(term))
                    out.write(" ")
                    flag=0
                    list1.remove(term)
            else:
                out.write("{0}".format(term))
                out.write("\n")
                flag=1
    return

def sum_words(data):

    start=open(data).read()

    array = []
    wordlist=start.split()
    for word in wordlist:
        array.append(word)

    sum1=int(array[1])
    i=1
    half=len(array)/2

    while (i<len(array)):
        i=i+2
        if (i<len(array)):
            sum1=sum1+int(array[i])
    return sum1

def calc_posprob(sentence,file1,file2):
    prob_p =math.log2(pos_count_sep/(pos_count_sep+neg_count_sep))

    voca=open(file1).read()
    vocab=voca.split()
    with open(file1) as f:
        vocab_len= sum(1 for _ in f)

    pos_word=open(file2).read()
    pos_words=pos_word.split()
    #with open(file1) as f:
    #    total_pos= sum(1 for _ in f)
    total_pos=sum_words(file2)

    for word in sentence:
        if word in vocab:
            if word in pos_words:
                index= pos_words.index(word)
                count= int(pos_words[index+1])
                prob_1= math.log2(count+1/(total_pos+vocab_len))
                prob_p= prob_p+prob_1
        else:
            prob_1 = math.log2(1/(total_pos+vocab_len))
            prob_p= prob_p+prob_1
    return prob_p

def calc_negprob(sentence,file1,file2):
    prob_n =math.log2(neg_count_sep/(pos_count_sep+neg_count_sep))
    voca=open(file1).read()
    vocab=voca.split()
    with open(file1) as f:
        vocab_len= sum(1 for _ in f)

    neg_word=open(file2).read()
    neg_words=neg_word.split()
    #with open(file1) as f:
    #    total_neg= sum(1 for _ in f)
    total_neg=sum_words(file2)

    for word in sentence:
        if word in vocab:
            if word in neg_words:
                index= neg_words.index(word)
                count= int(neg_words[index+1])
                prob_1= math.log2(count+1/(total_neg+vocab_len))
                prob_n= prob_n+prob_1
        else:
            prob_1 = math.log2(1/(total_neg+vocab_len))
            prob_n= prob_n+prob_1
    return prob_n
def multinomial_naive_bayes(data,test):

    separation(data)
    vocabulary(data,"train_res.txt")
    vocabulary("positive_part.txt","pos_res.txt")
    vocabulary("negative_part.txt","neg_res.txt")

    sum_neg=sum_words("neg_res.txt")
    tp=0
    tn=0
    fp=0
    fn=0
    test_file = open(test)
    #k=1
    for line in test_file:
        sentence = line.split()
        if sentence[0]=='+':
            original = 1
            sentence.remove('+')
        else:
            original =0
            sentence.remove('-')
        pos_prob = calc_posprob(sentence,"train_res.txt","pos_res.txt")
        neg_prob = calc_negprob(sentence,"train_res.txt","neg_res.txt")
        if pos_prob>neg_prob:
            detected =1
        else:
            detected =0

        #k=k+1
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


i=0
j=25
p=1
calc_avg_acc=[]
while i<=250 and j<=250:
    train_data=open("dataset_combined.txt","r")
    pos_count=0
    neg_count=0
    iter_train=""
    iter_test=""
    for line in train_data:
        words=line.split()
        if words[0]=='+':
            pos_count +=1
        elif words[0]=='-':
            neg_count +=1
        if words[0]=='+' and pos_count > i and pos_count <= j:
            iter_test += line
        elif words[0]=='-' and neg_count > i and neg_count <= j:
            iter_test += line
        else:
            iter_train += line

    train_data.close()
    training= open("train_opr.txt","w")
    testing=open("test_opr.txt","w")

    for k in range(len(iter_train)):
        training.write(iter_train[k])
    for k in range(len(iter_test)):
        testing.write(iter_test[k])
    training.close()
    testing.close()

    accuracy=multinomial_naive_bayes("train_opr.txt","test_opr.txt")
    print("Accuracy of iteration",p ,"is ")
    print(accuracy*100)
    calc_avg_acc.append(accuracy)
    i=i+25
    j=j+25
    p=p+1
print("Average Accuracy")
print((sum(calc_avg_acc)/len(calc_avg_acc))*100)
