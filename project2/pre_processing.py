# This python file contains functions for preprocessing raw datasets

import re
import nltk

from textblob import TextBlob

contractions_dict = {
    """
        DESCRIPTION:
        Dictionary used for expanding contractions
    """
    
    "didn\'t": "did not", "don\'t": "do not",
    "ain't": "am not",
    "aren't": "are not",
    "can't": "can not",
    "can't've": "can not have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he had",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "i'd": "i would",
    "i'd've": "i would have",
    "i'll": "i will",
    "i'll've": "i will have",
    "i'm": "i am",
    "i've": "i have",
    "isn't": "is not",
    "it'd": "it would",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she had",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so as",
    "that'd": "that would",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there would",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they shall have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who has / who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you had / you would",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have"
}



def hasNumbers(inputString):
    """
    DESCRIPTION: Returns true or false if it has numbers
    INPUT:
            inputString: a string
    OUTPUT:
            Boolean that says if it has a number
    """
    return bool(re.search(r'\d', inputString))


def filter_digits(tweet):
    """
    DESCRIPTION: Replaces digits with tag <number>
    INPUT:
            tweet:  a string
    OUTPUT:
            a tweet where a digit is replaced by the tag <number>
            (e.g. "I laugh 1234 times" outputs "I laugh <number> times")
    """

    t = []
    for w in tweet.split():
        try:
            num = re.sub('[,\.:%_\-\+\*\/\%\_]', '', w)
            float(num)
            t.append("<number>")
        except:
            t.append(w)
    return (" ".join(t)).strip()



def remove_words(tweet):
    """
    DESCRIPTION: filters repeated tags (user, url and number) from a tweet
    INPUT:
            tweet:  a string
    OUTPUT:
            a tag-filtered tweet as a python string
            (e.g. "user believes today is friday number" outputs "believes today is friday")
    """

    removal_list = ["user", "url", "number"]
    word_list = tweet.split()
    tweet = ' '.join([i for i in word_list if i not in removal_list])
    return tweet


def replace_moreletters(tweet):
    """
    DESCRIPTION: Replaces by 2 repeated letters when there are more than two repeated letters
    INPUT:
            tweet:  a string
    OUTPUT:
            A tweet without letters repeating more than two times
            (e.g. "I am haaaaaapy" outputs "I am haapy")
    """

    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", tweet)


def remove_punctuation(tweet):
    """
    DESCRIPTION: Filters punctuation from a tweet
    INPUT:
            tweet: a string
    OUTPUT:
            punctuation-filtered tweet as a python string without hash, exclamation and apostrophe marks.
            (e.g. "I .... feel down" outputs "I feel down")
    """

    temp = []
    name1 = tweet.split()
    for i in name1:
        clean = re.split('[-:_*^<>/{}()<>",?&.$%@~!]', i)
        tweet = " ".join(clean)
        temp.append(tweet)
    out = " ".join(temp)
    return out




def split_number_text(tweet):
    """
    DESCRIPTION: Splits numbers and characters in a word
    INPUT:
            tweet: a string
    OUTPUT:
            tweet with text and numbers split
            (e.g. "123test55" outputs "123 test 55")
    """
    link = []
    temp = tweet.split()
    for r in temp:
        if hasNumbers(r):
            temp = re.split('(\d+)', r)
            for j in temp:
                if re.search('[a-zA-Z]', j) and len(j) >1 or j=='i' or j=='I':
                    link.append(j)
        elif len(r) > 1 or r=='i' or r=='I':
            link.append(r)
        elif r == '#' or r == '!' or r == "+":
            link.append(r)
    tweet = " ".join(link)
    return tweet


def separate_hash(tweet):
    """
    DESCRIPTION: Separates hash symbol from words
    INPUT:
            tweet: a tweet as a python string
    OUTPUT:
            tweet with hash symbols and words separated
            (e.g. "#hello" outputs "# hello")
    """
    tweet = " ".join(re.split('(\W#)', tweet))
    return tweet


def interpret_emoji(tweet):
    """
    DESCRIPTION: 
                transforms emoticons to sentiment tags e.g :) --> <smile>
    INPUT: 
            tweet: a tweet as a python string
    OUTPUT: 
            transformed tweet as a python string
            (e.g. "today is friday :-) <3" outputs "today is friday <smile> <heart>")
    """
    # Construct emojis
    hearts = ["<3", "♥"]
    eyes = ["8", ":", "=", ";"]
    nose = ["'", "`", "-", r"\\"]
    smilefaces = []
    lolfaces = []
    sadfaces = []
    neutralfaces = []

    for e in eyes:
        for n in nose:
            for s in ["\)", "d", "]", "}", ")"]:
                smilefaces.append(e + n + s)
                smilefaces.append(e + s)
            for s in ["\(", "\[", "{", "(", "["]:
                sadfaces.append(e + n + s)
                sadfaces.append(e + s)
            for s in ["\|", "\/", r"\\", "|"]:
                neutralfaces.append(e + n + s)
                neutralfaces.append(e + s)
            # reversed
            for s in ["\(", "\[", "{", "[", "("]:
                smilefaces.append(s + n + e)
                smilefaces.append(s + e)
            for s in ["\)", "\]", "}", ")", "]"]:
                sadfaces.append(s + n + e)
                sadfaces.append(s + e)
            for s in ["\|", "\/", r"\\", "|"]:
                neutralfaces.append(s + n + e)
                neutralfaces.append(s + e)
            lolfaces.append(e + n + "p")
            lolfaces.append(e + "p")

    smilefaces = set(smilefaces)
    lolfaces = set(lolfaces)
    sadfaces = set(sadfaces)
    neutralfaces = set(neutralfaces)
    t = []
    for w in tweet.split():
        if (w in hearts):
            t.append("<heart>")
        elif (w in smilefaces):
            t.append("<smile>")
        elif (w in lolfaces):
            t.append("<lol>")
        elif (w in neutralfaces):
            t.append("<neutral>")
        elif (w in sadfaces):
            t.append("<sad>")
        else:
            t.append(w)
    return (" ".join(t)).strip()


def replace_hashtag(tweet):
    """
    DESCRIPTION: Replaces hashtags (e.g. #iloveyou) by the tag "<hashtag>"
    INPUT:
            tweet: a tweet as a python string
    OUTPUT:
            modified tweet, replacing hashtags with the tag <hashtag>
            (e.g. "today is friday #hapoy" outputs "today is friday <hashtag>")
    """
    sentence = []
    line = tweet.split()
    for w in line:
        if "#" in w and len(w) > 1:
            sentence.append("<hashtag>")
        else:
            sentence.append(w)
    tweet = ' '.join(sentence)
    return tweet


def one_space(tweet):
    """
    DESCRIPTION: Removes extra spaces between words, ensures only one space is left
    INPUT:
            tweet: a tweet as a python string
    OUTPUT:
            modified tweet, containing only one space between words
            (e.g. "today is     friday" outputs "today is friday")
    """
    tweet = re.sub("\s\s+", " ", tweet)
    return tweet


def hashtag_remove(tweet):
    """
    DESCRIPTION: Removes # of sentences
    INPUT:
            tweet: a tweet as a python string
    OUTPUT:
            modified tweet, replacing hashtags with a space
    """
    
    sentence = []
    words = tweet.split()
    for j in words:
        if "#" in j:
            j = j.replace("#", "")
            sentence.append(j)
    tweet = ' '.join(sentence)
    return tweet

##Code modified from https://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python
contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()))
def expand_contractions(s, contractions_dict=contractions_dict):
    """
    DESCRIPTION: Expands contractions of all words (contracted) in the tweet
    INPUT:
            tweet: a tweet as a python string
    OUTPUT:
            modified tweet, replacing contracted words by their expanded version
            (e.g. "don't do that, today isn't friday" outputs "do not do that, today is not friday")
    """
    
    def replace(match):
        return contractions_dict[match.group(0)]
    return contractions_re.sub(replace, s)









