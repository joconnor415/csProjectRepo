'''
Created on Jan 31, 2013

@author: jeremiahoconnor
'''
import cPickle as pickle
import sys
import pickle
import os
import collections
import sys
import os.path
import re
import string

#wf optional dictionary being passed in, 
def wordfreq(instr, wf=None, stripPunc=True, toLower=True) :
    try:
        f= open(instr)
        word_file= f.read()
        
        if stripPunc:
            word_file= word_file.translate(None, string.punctuation)
        if toLower:
            word_file= word_file.lower()
        
        word_array= word_file.split()
        
        count= collections.Counter()
        for word in word_array:
            count[word]+=1
        wc= dict(count)
        
        f.close()
        if wf==None:
            return wc
        else:
            for x in wf.keys():
                if wc.has_key(x):
                    wc[x]+=wf[x]
                else:
                    wc[x]= wf[x]
            return wc
        
    except(IOError), e:
        print "File not Found", e

#wordfreq {--nostrip --noConvert --pfile=outfile} file 
def main():

    bool_no_strip=True
    bool_no_lower= True
    arg_list= (sys.argv)
    outfile=""
    wf=None
    infile= arg_list[-1]

    for x in arg_list:
        if x== ("--nostrip"):
            bool_no_strip= False
        if x== ("--noConvert"):
            bool_no_lower= False
        if x.startswith("--pfile"):
            outfile= x[8:]
    
    wf=wordfreq(infile, wf, bool_no_strip, bool_no_lower)

    if outfile!="":
        if (os.path.isfile(outfile)):
            f2= open(outfile, 'r+')
            try:
                pic_dict = pickle.load(f2)
                for key in wf.keys():
                    if pic_dict.has_key(key):
                        wf[key]+=pic_dict[key]
                    else:
                        wf[key]= pic_dict[key]
            except (EOFError):
                print "EOF Error"
        f2= open (outfile, 'w')
        pickle.dump(wf, f2)
        f2.close()
        #print wf
    else:
        print wf

if __name__ == '__main__': main()
