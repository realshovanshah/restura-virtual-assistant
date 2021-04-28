import numpy as np
import nltk

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    # split sentence into smaller list of words/tokens
    # here we use the 'punkt' tokenizer
    return nltk.word_tokenize(sentence)


def stem(word):
    # find the root form or the stem of the word
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    '''
    list of - 1 if the word exists in the sentence else 0
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    '''
    # # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag