import nltk
from urllib import urlopen
import string
import collections
import math
from nltk.stem import PorterStemmer
import sys
import langid
from nltk import cluster
import operator


"""Detects language of the webpage after HTML is cleaned."""
def detect_language(doc):
	raw = nltk.clean_html(doc).lower()
	result= langid.classify(doc) #returns tuple (language, score)
	return result[0]

"""Create the cache of corpus' to test against."""
def build_corpus_cache():
	milton_corpus= nltk.corpus.gutenberg.words('milton-paradise.txt')
	melville_corpus= nltk.corpus.gutenberg.words('melville-moby_dick.txt')
	macbeth_corpus= nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
	carroll_corpus= nltk.corpus.gutenberg.words('carroll-alice.txt')
	hamlet_corpus= nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
	return [milton_corpus, melville_corpus, macbeth_corpus, carroll_corpus, hamlet_corpus]

"""Get stopwords in language of HTML document"""
def get_lang_stopset(country_code):
	lang_dict= {"en":"english", "fr":"french", "ru":"russian", "es":"spanish", "it":"italian"}
	language= lang_dict[country_code]
	shakespeare_stop_words= set(["thou", "come", "first", "shall", "enter", "thee", "yet", "good", "hath", "time", "make", "well", "would", "ross"])
	stop_set= set(nltk.corpus.stopwords.words(language))
	stop_set.update(shakespeare_stop_words)
	return stop_set

"""Clean HTML document"""
def process_html_doc(html_doc, stop_set):
	raw = nltk.clean_html(html_doc).lower()
	raw = raw.translate(string.maketrans("",""), string.punctuation)
	tokens= nltk.word_tokenize(raw)
	return prep_data(tokens, stop_set)	

"""Prepare: remove stopwords, stem, get counts"""
def prep_data(doc, stop_set):	
	content = [w.lower() for w in doc if w.lower() not in stop_set]
	stemmer= PorterStemmer()
	content = [stemmer.stem(w) for w in content]
	counts= collections.Counter(content)
	return counts

"""Prepare corpus list"""
def clean_and_stem_corpus_list(corpus_list, stop_set):
	result= []
	for corpus in corpus_list:
		counts= prep_data(corpus, stop_set)
		result.append(counts)
	return result

"""Make keys in appropriate dictionaries equal"""
def get_similar_keys(html_dict, corpus_dict):
	
	inters= set(html_dict.keys()) & set(corpus_dict.keys())

	html_int_dict= {}
	corpus_int_dict= {}
	for k, v in html_dict.items():
		if k in inters:
			html_int_dict[k]= v

	for k, v in corpus_dict.items():
		if k in inters:
			corpus_int_dict[k]= v

	html_tups= [(k,v) for k, v in html_int_dict.iteritems()]
	corpus_tups= [(k,v) for k, v in corpus_int_dict.iteritems()]
	html_tups.sort(key=lambda tup: tup[0])
	corpus_tups.sort(key=lambda tup: tup[0])

	html_tup_vals= [a[1] for a in html_tups]
	corpus_tup_vals= [a[1] for a in corpus_tups]
	return html_tup_vals, corpus_tup_vals

"""Get Cosine Distance between contents of HTML document and corpus"""
def get_cosine_distance(html_t_vals, corpus_t_vals):
	res=cluster.util.cosine_distance(html_t_vals, corpus_t_vals)
	return res

"""Calculate Term Frequency and Document Frequency and return 10 most common tokens"""
def calc_tf_idf(html_dict, corpus_dict):
	tf_idf_dict= {}
	for k, tf in html_dict.items():
		if k in corpus_dict:
			idf = math.log(len(html_dict)/ float((1.0 + corpus_dict[k])))
		else:
			#laplace smoothing, add one estimation
			idf= math.log((len(html_dict)+1.0)/len(html_dict))
		tf_idf_dict[k]= (tf*idf)
		#filter out
		tf_idf_dict.pop("thi", None)
	return collections.Counter(tf_idf_dict).most_common(10)

"""Create Note cache to test against for 2nd Question"""
def create_notebooks():

	basketball_note = urlopen("http://en.wikipedia.org/wiki/Basketball").read()
	peanut_butter_note = urlopen("http://en.wikipedia.org/wiki/Peanut_butter").read()
	shark_note= urlopen("http://en.wikipedia.org/wiki/Great_white_shark").read()
	dog_note= urlopen("http://en.wikipedia.org/wiki/Dog").read()
	shark2_note= urlopen("http://en.wikipedia.org/wiki/Bull_shark").read()
	return [("basketball", basketball_note), ("peanut_butter", peanut_butter_note), ("dog",dog_note), ("Great White Shark",shark_note), ("Bull Shark",shark2_note)]



if __name__== '__main__':

	
	#url = "http://bleacherreport.com/articles/2027786-the-new-manny-pacquiao-will-aging-veteran-continue-to-find-ways-to-win"
	corpus_cache= build_corpus_cache()
	#url = "http://en.wikipedia.org/wiki/Macbeth"
	#url = "http://shakespeare.mit.edu/macbeth/full.html"
	url= "http://www.wikisummaries.org/Macbeth"
	html_doc = urlopen(url).read()
	language= detect_language(html_doc)
	stop_set=  get_lang_stopset(language)
	clean_html_doc= process_html_doc(html_doc, stop_set)
	clean_corpus_list= clean_and_stem_corpus_list(corpus_cache, stop_set)
	d= {}
	counter = 0
	min_res= 1.1
	index= 0
	for corpus in clean_corpus_list:
		html_vals, corpus_vals = get_similar_keys(clean_html_doc, corpus)
		result = get_cosine_distance(html_vals, corpus_vals)
		print result

		if result < min_res:
			index= counter
			min_res= result
		counter+=1
	top_ten= calc_tf_idf(clean_html_doc, clean_corpus_list[index])
	print "\n"
	print "*************************Results for Question #1:************************"
	print "10 words that best capture the meaning/content of text on page:"
	print url
	c=1
	for term in top_ten:
		print str(c)+". "+ term[0]
		c+=1


	notebooks= create_notebooks()
	url = "http://en.wikipedia.org/wiki/Tiger_shark"
	html_doc = urlopen(url).read()
	language= detect_language(html_doc)
	stop_set=  get_lang_stopset(language)
	clean_html_doc= process_html_doc(html_doc, stop_set)
	
	suggestions= {}
	for notebook in notebooks:
		clean_html_note= process_html_doc(notebook[1], stop_set)
		html_vals, corpus_vals = get_similar_keys(clean_html_doc, clean_html_note)
		result = get_cosine_distance(html_vals, corpus_vals)
		suggestions[notebook[0]]=result

	suggestions = sorted(suggestions.iteritems(), key=operator.itemgetter(1))
	print "*************************Results for Question #2:************************"
	print "Clipped Note from: http://en.wikipedia.org/wiki/Tiger_shark"
	print "Suggested Notebooks:", suggestions[0][0]+ ", "+  suggestions[1][0]
	print "*************************************************************************"
	print "\n"




