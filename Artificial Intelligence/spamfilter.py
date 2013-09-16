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
      self.dict = {}
      self.numEmail = 0  
      
    def trainOn(self, path):
        os.chdir(path)
        numEmail = 0
        for file in os.listdir("./"):
            numEmail += 1
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
                        if( w in self.dict): self.dict[w] += 1
                        else : self.dict[w] = 1 
        os.chdir("../")
        self.numEmail= numEmail
        
def prob(email, spamSet, hamSet):
    num = 0
    spamScore = log(spamSet.numEmail/float(spamSet.numEmail + hamSet.numEmail))
    hamScore = log(hamSet.numEmail/float(spamSet.numEmail + hamSet.numEmail))
    try:
        f=open(email)
    except:
        print "Can't find file this " + email 
        sys.exit(2)
                
    table = string.maketrans("", "")
    for l in f:
        l = l.translate(table, string.punctuation)
        words =  str.split(l)
        for w in words:
            w = string.lower(w)
            if ( len(w) > 2 and len(w) < 20 and w not in stopwords):
                # if it's in both of them 
                if( w in spamSet.dict and w in hamSet.dict):
                    sScore = spamSet.dict[w]
                    hScore = hamSet.dict[w]
                    if( spamScore == 0 ): 
                        spamScore = log(float(sScore)/spamSet.numEmail)
                    else: 
                        spamScore = spamScore + log(float(sScore)/spamSet.numEmail)

                    if( hamScore == 0 ): 
                        hamScore = log(float(hScore)/hamSet.numEmail)
                    else: 
                        hamScore = hamScore + log(float(hScore)/hamSet.numEmail)
                    
                # if the word is only in hamSet then apply .99 and .01 to spam
                elif( w in hamSet.dict):
                    if( spamScore == 0 ): 
                        spamScore = log(.01)
                    else: 
                        spamScore = spamScore + log(float(.01))
                        
                    if( hamScore == 0):
                        hamScore = log(0.99)
                    else: 
                        hamScore = hamScore + log(.99)
                elif( w in spamSet.dict):
                    if( spamScore == 0 ): 
                        spamScore = log(.99)
                    else: 
                        spamScore = spamScore + log(float(.99))
                        
                    if( hamScore == 0):
                        hamScore = log(0.01)
                    else: 
                        hamScore = hamScore + log(.01)
                # if not in both, we will take it as ham since spam words 
                # tends to be all too fimiliar
                else:
                    if( hamScore == 0):
                        hamScore = log(0.4)
                    else: 
                        hamScore = hamScore + log(.4)

    return spamScore, hamScore
                    

def test(testSet, spamTSet, hamTSet):
    spamC = 0
    hamC = 0
    os.chdir(testSet)
    for file in os.listdir("./"):
        spam, ham = prob(file, spamTSet, hamTSet)
    
        if( spam > ham):
            spamC +=1    
        if(ham > spam):
            hamC +=1
    os.chdir("../")
    return spamC, hamC

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
    hamTSet.trainOn(hamtrain)
    spamTSet.trainOn(spamtrain)
    
    spamC, hamC = test(hamtest, spamTSet, hamTSet)
    spamC1, hamC1 = test(spamtest, spamTSet, hamTSet)
    
    
    print """ 
Size of ham training set: %d emails
Size of spam training set: %d emails:
Percentage of ham classified correctly: %.1f
Percentage of spam classified correctly: %.1f
Total accuracy: %.1f
False Positives: %.1f
"""   % (hamTSet.numEmail, spamTSet.numEmail, 
            float(hamC)/(hamC+spamC)*100, float(spamC1)/(hamC1+spamC1)*100,
            (float(hamC)/(hamC+spamC)+ float(spamC1)/(hamC1+spamC1))*50,
            100 - float(hamC)/(hamC+spamC)*100)







"""
def getTset(tSet_name):
    trainingSet = TrainingSet()
    trainingSet.trainOn("/Users/ganbilegbor/Desktop/Spring 2013/cs662/Eclipse/Assignment6/" + tSet_name)
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





        

        


