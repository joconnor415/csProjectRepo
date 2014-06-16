1) If you were given the HTML contents of a single web page, how would you determine the 10 words that best capture the meaning/content of the text on the page? How would your approach change if the page were written in a foreign language that you couldn't understand?

     For my implementation of this question, I decided to use the “Bag of Words” model to represent the contents of the web page and the different corpus'. I used the ML/Text Processing libraries NLTK for text analysis, and LangID for language detection.
      For the first part of question #1, determining the 10 words that best capture meaning/content of the page, I tested the HTML contents of Macbeth web page (copy of text): http://shakespeare.mit.edu/macbeth/full.html”, in comparison with 5 of the books Paradise Lost- Milton, Moby Dick- Melville, Macbeth- Shakespeare, Alice in Wonderland- Carroll, Hamlet- Shakespeare, from NLTK's Gutenberg corpus. The 'proof of concept’ for these questions was to test the HTML contents of a Macbeth wikipedia article or version of the text and if the the program works correctly it will come back with the most important words of the webpage related to Macbeth. First I retrieved the web page and identified the language using the python langID library. This library uses Naive Bayes and byte N-grams for identifying the language. I tested that I was able to retrieve web pages in many languages and langID's detection of the correct language is very accurate. The corpus' of texts I cached is only in English, but ideally I would keep a corpus of all the texts in each language that I want my program to be able to handle. I then retrieve the two letter language ID, and pass that to NLTK’s stop words, in order to get the stop words in correct language to filter out of my document. I would then clean the data of the web page and also all the texts in the corpus. I  strip out all HTML tags out of the document, strip out all the punctuation, convert all words to lower case, filter out the stop words and also my own list of "Shakespearean stop words". Then I do stemming for the words in HTML document and the corpuses: word suffixes such as pluralization, past tense, -ing are removed, and consolidating all the word with similar meanings (Ex. happiness —> happy). Some advantages of stemming are when counting words, stemming lets you correctly count different forms of a word. Some disadvantages are dealing with abnormal forms, potential misgrouping (ex. university, universal). I then go through and create the vectors which will be passed to the cosine distance function. I then calculate the cosine distance to identify the corpus that is most similar to the HTML document. I chose to use TF-IDF (Term Frequency and Inverse Document Frequency): the product of TF weight and IDF weight because it’s good for ranked information retrieval. I calculate the TF-IDF with Laplace smoothing, between the HTML document and the corpus with the least cosine distance. I then store those terms mapping to the TF-IDF scores in a dictionary and return the 10 most meaningful terms.
    There are a number of ways to do language detection. One “quick hack” is to filter out the stop words or common words of each language from the HTML document, then generate the stop words or common words in each language and match them up to a stored corpus of words in that language. PyEnchant would be a good tool to create dictionaries of words in different languages to do lookups against. NLTK provides stop word lists in multiple languages so that would be another method of checking languages. Other options are doing bi-gram and tri-gram character tagging and then comparing to a corpus in that language. Bi-gram or tri-gram word tagging will work for many languages, but for languages like Chinese and Japanese it’s better to use bigram, trigram by characters. I used LangID in my code, but if I had to create my own I would do it using a form of Bayesian inference: First, I will keep cache of all the texts in the corpus we are comparing against in however many languages we wish our application to support. To detect the language, I would count all the 2-grams in the document by characters. I would then estimate the probabilities for Language L with the formula: P(L)=  (count / number of 2 grams). The assumption I’m making is that different languages have specific 2-grams. After finding all the  2-grams in the document, I call this set s. For each language L, the likelihood that the document's language is L = P[L](s[1]) * P[L](s[2]) * ….P[L](s[n]). After testing all languages in the cached language corpus, the language that comes back with the maximum likelihood is the language of the document.
     My program successfully outputs the most meaningful words. It successfully identifies the play’s most important characters like Macbeth, Macduff, Lady Macbeth, Banquo, Duncan, and Malcom. It also successfully identifies the major themes of the play: witches, illness (mental), fear, ladi (stemmed version for Lady, meaning women play a big role in play) and murder. I provided five test cases all returning the similar results.


2. How might you use the contents of a user's Evernote account to automatically suggest which notebook or tags should be assigned to a new note clipped into the account from the web?*
     I used the solution from the first problem to solve this question. Instead of using NLTK’s Gutenberg corpus’ from the first question, I cached the HTML contents of 5 URLs from wikipedia to represent the user's notebooks (corpus), cleaned and stemmed them, and then created the count vectors. To represent the "clipped content”, I would just get the HTML contents from the web page of the clipped content. And then basically I used the same method of finding the cosine distances between the clipped document and the notebooks. I then took the top 2 in this case because I was only testing out 5 webpages against the clipped content’s page. But basically I can just either take the top k notebooks as suggestions, or set a cosine similarity threshold to determine how close you want the suggested notebooks to be to your clipped content and compare that to the cosine distance between each corpus and the HTML contents of the clipped content’s source. I used the the wikipedia article about tiger sharks to represent the "new note content" clipped from the web. I then used 5 articles from wikipedia 2 about sharks, 1 about basketball, 1 about peanut butter, 1 about dogs. In the end I was able to successfully suggest notebooks related to the clipped content. In cases with the no notes or very small amount of notes, I would set a limit to how much content (or how many words) are in a notebooks, so as to reduce false positives and anything that might not be relevant to get the most accurate suggestions.
     Some other options would be comparing most frequent words in the page where the note was clipped from, and compare it against notebook tags. However that’s assuming that the user has taken time to mark the appropriate tags for each notebook. Along the same lines, is using the above method to find the most meaningful words of the notebook and have this sync periodically over the course of the day or every time there are changes to a notebook, and use those as “tags”, and compare those to the top meaningful words from the clipped content’s page.
     The output of the program is successful. When passed in "clipped content" from wikipedia about tiger sharks, it is able to suggest other notebooks related to sharks.


Output for 5 Tests on Different URLs related to Macbeth:

*************************Results for Question #1:************************
10 words that best capture the meaning/content of text on page:
http://en.wikipedia.org/wiki/Macbeth
1. macbeth
2. shakespear
3. play
4. witch
5. ladi
6. perform
7. murder
8. william
9. king
10. banquo
*************************Results for Question #2:************************
Clipped Note from: http://en.wikipedia.org/wiki/Tiger_shark
Suggested Notebooks: Great White Shark, Bull Shark
*************************************************************************

*************************Results for Question #1:************************
10 words that best capture the meaning/content of text on page:
http://shakespeare.mit.edu/macbeth/full.html
1. macbeth
2. macduff
3. murder
4. ladi
5. witch
6. banquo
7. malcolm
8. ill
9. duncan
10. fear
*************************Results for Question #2:************************
Clipped Note from: http://en.wikipedia.org/wiki/Tiger_shark
Suggested Notebooks: Great White Shark, Bull Shark
*************************************************************************

*************************Results for Question #1:************************
10 words that best capture the meaning/content of text on page:
http://www.wikisummaries.org/Macbeth
1. macbeth
2. murder
3. kill
4. propheci
5. macduff
6. castl
7. witch
8. banquo
9. malcolm
10. son
*************************Results for Question #2:************************
Clipped Note from: http://en.wikipedia.org/wiki/Tiger_shark
Suggested Notebooks: Great White Shark, Bull Shark
*************************************************************************

*************************Results for Question #1:************************
10 words that best capture the meaning/content of text on page:
http://www.macbethonbroadway.com/macbeth-synopsis.html
1. macbeth
2. witch
3. play
4. king
5. shakespear
6. murder
7. curs
8. armi
9. malcolm
10. macduff
*************************Results for Question #2:************************
Clipped Note from: http://en.wikipedia.org/wiki/Tiger_shark
Suggested Notebooks: Great White Shark, Bull Shark
*************************************************************************

*************************Results for Question #1:************************
10 words that best capture the meaning/content of text on page:
http://www.william-shakespeare.info/shakespeare-play-macbeth.htm
1. shakespear
2. play
3. william
4. macbeth
5. witch
6. duncan
7. act
8. murder
9. work
10. macduff
*************************Results for Question #2:************************
Clipped Note from: http://en.wikipedia.org/wiki/Tiger_shark
Suggested Notebooks: Great White Shark, Bull Shark
*************************************************************************