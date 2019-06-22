########################################################################################################################
# Well, I'm Anirban. And I am learning NLP basics. In this project, I will execute the basics of NLP using NLTK that I
#  would be learning. Practise and also for future use.
# Resource link(s):
# 1: https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-
#    codes-in-python/
# 2: https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
# 3:
#
# Associate resources:
# a. POS Tags: https://www.nltk.org/book/ch05.html
########################################################################################################################
# Date: 21.06.2019
# Version: 0.1 [Draft]
########################################################################################################################
import nltk


def word_tokenise(text):
    # Word Tokens are basically the words in the text.
    from nltk.tokenize import word_tokenize
    word_tokens = word_tokenize(text)
    return word_tokens


def remove_stopwords(word_tokens):
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    custom_stop_words = ['RT', ':D', ':P', ':/']      # This should come from a custom file.
    symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '*', '(', ')', '-', '{', '}', '[', ']', '|', ':',
               ';', '"', '<', '>', ',', '.', '/', '?']

    # Removing Stop words and symbols.
    text_wo_stopwords = [w for w in word_tokens if not w in stop_words]
    text_wo_stopwords = [w for w in text_wo_stopwords if not w in custom_stop_words]
    text_wo_symbols = [w for w in text_wo_stopwords if not w in symbols]
    return text_wo_symbols


def text_stemmed(word_list):
    # Stemming words now
    from nltk.stem.wordnet import WordNetLemmatizer
    lem = WordNetLemmatizer()

    from nltk.stem.porter import PorterStemmer
    stem = PorterStemmer()

    final_words = []
    for w in word_list:
        #if str(lem.lemmatize(w, "v")) != w:
        #    print(w+" changed to >> "+str(lem.lemmatize(w, "v")))
        if str(stem.stem(w)) != w:
            #print("Stemmed word: " + str(stem.stem(w)))
            final_words.append(str(stem.stem(w)))
        else:
            final_words.append(w)
    #print(final_words)
    return final_words


# Constructing dependency trees -> I read the theory. I did not write a program to visualise it.

# POS Tagging:
def words_pos_tagged(word_list):
    from nltk import pos_tag

    #print("------------------\nPart of Speech tagged (from all words):\n")
    word_tagged = pos_tag(word_list)
    #print(word_tagged)
    return word_tagged

    # Observation: Once stemmed and/or lemmatised, the POS of the word is changing (which was preempted).
    # So we will take all tokenised words and not stem it for POS tagging, to not lose the original intent of the user.
    # List of tags: https://www.nltk.org/book/ch05.html


def return_noun_list(word_list):
    # Reading the POS tagging & printing the nouns:
    nouns = [w for w in word_list if w[1] == 'NN' or w[1] == 'NNS' or w[1] == 'NN$']
    return nouns


def create_n_grams(text, n):
    # Finding n grams
    words = text.split()
    ngrams = []
    for i in range(len(words)-n+1):
        ngrams.append(words[i:i+n])
    #print(ngrams)
    return ngrams


def text_chunking_1(text_pos_tagged):
    from nltk import  RegexpParser
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = RegexpParser(grammar)
    chunk = cp.parse(text_pos_tagged)
    return chunk


def text_chunking_2(text_pos_tagged):
    from nltk import RegexpParser
    # I did not understand how the grammar is made in the program.
    # The logic part I understood.
    grammar = r"""
              NP: {<DT|PP\$>?<JJ>*<NN|NNS|NN$>}
              {<DT|PP\$>?<VB|VBG><NN|NNS|NN$>} 
              {<VB|VBG|VBN>?<NN|NNS|NN$>} 
              {<NNP>+}               
              {<NN>+}
               """
    cp = RegexpParser(grammar)
    chunk = cp.parse(text_pos_tagged)
    return chunk


def return_NP(chunk):
    np_list = []
    for subtree in chunk.subtrees():
        if subtree.label() == 'NP':
            t = subtree
            t = ' '.join(word for word, pos in t.leaves())
            np_list.append(t)
    return np_list
