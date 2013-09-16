stopwords = {'all': True, 'six': True, 'less': True, 'being': True, 'indeed': True,
          'over': True, 'move': True, 'anyway': True, 'four': True, 'not': True,
          'own': True, 'through': True, 'yourselves': True, 'fify': True, 
          'where': True, 'mill': True, 'only': True, 'find': True, 
          'before': True, 'one': True, 'whose': True, 'system': True, 
          'how': True, 'somewhere': True, 'with': True, 'show': True, 
          'had': True, 'enough': True, 'should': True, 'to': True, 'must': True, 
          'whom': True, 'seeming': True, 'whole': True, 'under': True, 
          'ours': True, 'has': True, 'might': True, 'thereafter': True, 
          'latterly': True, 'do': True, 'them': True, 'his': True, 
          'around': True, 'than': True, 'get': True, 'very': True, 'de': True, 
          'none': True, 'cannot': True, 'every': True, 'whether': True, 
          'they': True, 'front': True, 'during': True, 'thus': True, 
          'now': True, 'him': True, 'nor': True, 'name': True, 'several': True, 
          'hereafter': True, 'always': True, 'who': True, 'cry': True, 
          'whither': True, 'this': True, 'someone': True, 'either': True, 
          'each': True, 'become': True, 'thereupon': True, 'sometime': True, 
          'side': True, 'two': True, 'therein': True, 'twelve': True, 
          'because': True, 'often': True, 'ten': True, 'our': True, 'eg': True, 
          'some': True, 'back': True, 'thickv': True, 'go': True, 
          'namely': True, 'towards': True, 'are': True, 'further': True, 
          'beyond': True, 'ourselves': True, 'yet': True, 'out': True, 
          'even': True, 'will': True, 'what': True, 'still': True, 'for': True, 
          'bottom': True, 'mine': True, 'since': True, 'please': True, 
          'forty': True, 'per': True, 'its': True, 'everything': True, 
          'behind': True, 'un': True, 'above': True, 'between': True, 
          'it': True, 'neither': True, 'seemed': True, 'ever': True, 
          'across': True, 'she': True, 'somehow': True, 'be': True, 
          'we': True, 'full': True, 'never': True, 'sixty': True, 
          'however': True, 'here': True, 'otherwise': True, 'were': True, 
          'whereupon': True, 'nowhere': True, 'although': True, 'found': True, 
          'alone': True, 're': True, 'along': True, 'fifteen': True, 
          'by': True, 'both': True, 'about': True, 'last': True, 
          'would': True, 'anything': True, 'via': True, 'many': True, 
          'could': True, 'thence': True, 'put': True, 'against': True, 
          'keep': True, 'etc': True, 'amount': True, 'became': True, 
          'ltd': True, 'hence': True, 'onto': True, 'or': True, 'con': True, 
          'among': True, 'already': True, 'co': True, 'afterwards': True, 
          'formerly': True, 'within': True, 'seems': True, 'into': True, 
          'others': True, 'while': True, 'whatever': True, 'except': True, 
          'down': True, 'hers': True, 'everyone': True, 'done': True, 
          'least': True, 'another': True, 'whoever': True, 'moreover': True, 
          'couldnt': True, 'throughout': True, 'anyhow': True, 'yourself': True, 
          'three': True, 'from': True, 'her': True, 'few': True, 
          'together': True, 'top': True, 'there': True, 'due': True, 
          'been': True, 'next': True, 'anyone': True, 'eleven': True, 
          'much': True, 'call': True, 'therefore': True, 'interest': True, 
          'then': True, 'thru': True, 'themselves': True, 'hundred': True, 
          'was': True, 'sincere': True, 'empty': True, 'more': True, 
          'himself': True, 'elsewhere': True, 'mostly': True, 'on': True, 
          'fire': True, 'am': True, 'becoming': True, 'hereby': True, 
          'amongst': True, 'else': True, 'part': True, 'everywhere': True, 
          'too': True, 'herself': True, 'former': True, 'those': True, 
          'he': True, 'me': True, 'myself': True, 'made': True, 
          'twenty': True, 'these': True, 'bill': True, 'cant': True, 
          'us': True, 'until': True, 'besides': True, 'whenever': True, 
          'below': True, 'anywhere': True, 'nine': True, 'can': True, 
          'of': True, 'your': True, 'toward': True, 'my': True, 
          'something': True, 'and': True, 'whereafter': True, 'give': True, 
          'almost': True, 'wherever': True, 'is': True, 'describe': True, 
          'beforehand': True, 'herein': True, 'an': True, 'as': True, 
          'itself': True, 'at': True, 'have': True, 'in': True, 'seem': True, 
          'whence': True, 'ie': True, 'any': True, 'fill': True, 'again': True, 
          'hasnt': True, 'inc': True, 'thereby': True, 'thin': True, 'no': True, 
          'perhaps': True, 'latter': True, 'meanwhile': True, 'when': True, 
          'detail': True, 'same': True, 'wherein': True, 'beside': True, 
          'also': True, 'that': True, 'other': True, 'take': True, 
          'which': True, 'becomes': True, 'you': True, 'if': True, 
          'nobody': True, 'see': True, 'though': True, 'may': True, 
          'after': True, 'upon': True, 'most': True, 'hereupon': True, 
          'eight': True, 'but': True, 'serious': True, 'nothing': True, 
          'such': True, 'why': True, 'a': True, 'off': True, 'whereby': True, 
          'third': True, 'nevertheless': True, 'up': True, 'noone': True, 
          'sometimes': True, 'well': True, 'amoungst': True, 'yours': True, 
          'their': True, 'rather': True, 'without': True, 'so': True, 
          'five': True, 'the': True, 'first': True, 'whereas': True, 
          'once': True}


import os
import sys
import string
from math import log
import getopt

class TrainingSet:
    def __init__(self):
      self.map = {}
      self.num_of_emails = 0  
      
    def train(self, path):
        os.chdir(path)
        num_of_emails = 0
        for file in os.listdir("./"):
            num_of_emails += 1
            try:
                f=open(file)
            except:
                print "Can't find file" + file 
                sys.exit(2)
                
            table = string.maketrans("", "")
            for l in f:
                l = l.translate(table, string.punctuation)
                words =  str.split(l)
                for w in words:
                    w = string.lower(w)
                    if ( len(w) > 2 and len(w) < 20 and w not in stopwords):
                        if( w in self.map): self.map[w] += 1
                        else : self.map[w] = 1 
        os.chdir("../")
 dict       self.num_of_emails= num_of_emails
        
def get_probability(email, spam_list, ham_list):
    num = 0
    spam_score = log(spam_list.num_of_emails/float(spam_list.num_of_emails + ham_list.num_of_emails))
    ham_score = log(ham_list.num_of_emails/float(spam_list.num_of_emails + ham_list.num_of_emails))
    try:
        f=open(email)
    except:
        print "Sorry cannot find the file: " + email 
        sys.exit(2)
                
    table = string.maketrans("", "")
    for l in f:
        l = l.translate(table, string.punctuation)
        words =  str.split(l)
        for w in words:
            w = string.lower(w)
            if ( len(w) > 2 and len(w) < 20 and w not in stopwords):
                # if it's in both of them 
                if( w in spam_list.map and w in ham_list.map):
                    s_score = spam_list.map[w]
                    h_score = ham_list.map[w]
                    if( spam_score == 0 ): 
                        spam_score = log(float(s_score)/spam_list.num_of_emails)
                    else: 
                        spam_score = spam_score + log(float(s_score)/spam_list.num_of_emails)

                    if( ham_score == 0 ): 
                        ham_score = log(float(h_score)/ham_list.num_of_emails)
                    else: 
                        ham_score = ham_score + log(float(h_score)/ham_list.num_of_emails)
                    
                # if the word is only in ham_list then apply .99 and .01 to spam
                elif( w in ham_list.map):
                    if( spam_score == 0 ): 
                        spam_score = log(.01)
                    else: 
                        spam_score = spam_score + log(float(.01))
                        
                    if( ham_score == 0):
                        ham_score = log(0.99)
                    else: 
                        ham_score = ham_score + log(.99)
                elif( w in spam_list.map):
                    if( spam_score == 0 ): 
                        spam_score = log(.99)
                    else: 
                        spam_score = spam_score + log(float(.99))
                        
                    if( ham_score == 0):
                        ham_score = log(0.01)
                    else: 
                        ham_score = ham_score + log(.01)
                # if not in both, we will take it as ham since spam words 
                # tends to be all too fimiliar
                else:
                    if( ham_score == 0):
                        ham_score = log(0.4)
                    else: 
                        ham_score = ham_score + log(.4)

    return spam_score, ham_score
                    

def test(testSet, spamTSet, hamTSet):
    spam_c = 0
    ham_c = 0
    os.chdir(testSet)
    for file in os.listdir("./"):
        spam, ham = get_probability(file, spamTSet, hamTSet)
    
        if( spam > ham):
            spam_c +=1    
        if(ham > spam):
            ham_c +=1
    os.chdir("../")
    return spam_c, ham_c

def usage():
    print "Usage: python ./nb.py --hamtrain=dir1 --spamtrain=dir2 --hamtest=dir3 --spamtest=dir4"
    

def getCommandLineInput(argv):
    
    try:                                
        opts, args = getopt.getopt(argv, "hsop:", 
                                ["hamtrain=", "spamtrain=", "hamtest=", "spamtest="])
    except getopt.GetoptError:          
        usage()                       
        sys.exit(2) 
                            
    for opt, arg in opts:                                 
        if opt == "--hamtrain":
            hamtrain = arg  
        if opt == "--spamtrain":
            spamtrain = arg
        if opt == "--hamtest":
            hamtest = arg  
        if opt == "--spamtest":
            spamtest = arg 
            
    return hamtrain, spamtrain, hamtest, spamtest

# python ./nb.py --hamtrain=dir1 --spamtrain=dir2 --hamtest=dir3 --spamtest=dir4
# example output
# Size of ham training set: 500 emails
# Size of spam training set: 700 emails:
# Percentage of ham classified correctly: 98.2
# Percentage of spam classified correctly: 97.0
# Total accuracy: 97.5
# False Positives: 1.8

if __name__ == '__main__' :  
     
    hamtrain, spamtrain, hamtest, spamtest = getCommandLineInput(sys.argv[1:])
    
    hamTSet = TrainingSet()
    spamTSet = TrainingSet()
    hamTSet.train(hamtrain)
    spamTSet.train(spamtrain)
    
    spam_c, ham_c = test(hamtest, spamTSet, hamTSet)
    spam_c1, ham_c1 = test(spamtest, spamTSet, hamTSet)
    
    
    print """ 
Size of ham training set: %d emails
Size of spam training set: %d emails:
Percentage of ham classified correctly: %.1f
Percentage of spam classified correctly: %.1f
Total accuracy: %.1f
False Positives: %.1f
"""   % (hamTSet.num_of_emails, spamTSet.num_of_emails, 
            float(ham_c)/(ham_c+spam_c)*100, float(spam_c1)/(ham_c1+spam_c1)*100,
            (float(ham_c)/(ham_c+spam_c)+ float(spam_c1)/(ham_c1+spam_c1))*50,
            100 - float(ham_c)/(ham_c+spam_c)*100)







"""
def getTset(tSet_name):
    trainingSet = TrainingSet()
    trainingSet.train("/Users/ganbilegbor/Desktop/Spring 2013/cs662/Eclipse/Assignment6/" + tSet_name)
    return trainingSet
    
spam = ["spam", "spam_2"]
ham = ["easy_ham", "easy_ham_2", "hard_ham"]

spamTset = [getTset("spam") , getTset("spam_2")]
hamTset= [getTset("easy_ham"), getTset("easy_ham_2") , getTset("hard_ham")]

spamTi = 0
for s in spam:
    hamTi = 0
    for h in ham:
        for spamT in spam:
            if(spamT != s):
                spamR, hamR = test(spamT, spamTset[spamTi], hamTset[hamTi])
                print "--------------------------------------------------------"
                print "test: %s, Tsets: %s, %s "      % (spamT, s, h) 
                print " Result: spam-> %d, ham-> %d"   % (spamR, hamR)
                print "--------------------------------------------------------"
        for hamT in ham:
            if(hamT != h):     
                spamR, hamR = test(hamT, spamTset[spamTi], hamTset[hamTi])
                print "--------------------------------------------------------"
                print "test: %s, Tsets: %s, %s "      % (hamT, s, h) 
                print " Result: spam-> %d, ham-> %d"   % (spamR, hamR)
                print "--------------------------------------------------------"
        hamTi +=1
    spamTi +=1


"""





        

        


