import nltk
import get_text_from_url
import basics

link = 'http://www.anirbansaha.com/volunteer-berlin-buzzwords/'

# Text fetched from the first paragraph of a custom WordPress Blog link. #scraping.
text = get_text_from_url.get_text_from_link(link)
text = text.lower()
print(text)

text_words = basics.word_tokenise(text)
print(text_words)

# Text without stopwords.
text_wo_stopwords = basics.remove_stopwords(text)
print(text_wo_stopwords)

# Text with words stemmed.
text_w_stemmed_words = basics.text_stemmed(text_wo_stopwords)

# Text with POS tagged.
text_pos_tagged = basics.words_pos_tagged(text_words)
print(text_pos_tagged)

# I do not know why I am doing this part. LOL.
# Maybe to check how to read the Tagged list.
# Nouns extracted from the text.
nouns = basics.return_noun_list(text_pos_tagged)
unique_nouns = set(nouns)
print(set(unique_nouns))


# Create n-grams from the text
n_grams_list = basics.create_n_grams(text, 2)
print(n_grams_list)
