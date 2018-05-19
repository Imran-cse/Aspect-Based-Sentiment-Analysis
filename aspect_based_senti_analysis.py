import math, string, re, nltk
import csv
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
from collections import Counter
from nltk.corpus import sentiwordnet as swn
import sentiment

pos_tag_review = {}
bigrams_dic = {}
trigrams_dic = {}
aspect_opinion = {}
rule = {}
aspect_dic = dict()

REGEX_REMOVE_PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))

not_list = ['no', 'nor', 'never', 'not', 'n\'t','don\'t',  'ain', 'aren', 'couldn', 'didn', 'doesn',
            'hadn', 'hasn', 'haven', 'isn', 'mightn', 'mustn', 'needn', 'shouldn', 'wasn', 'weren', 'won\'t', 'wouldn']
class sentiAnalyzer(object):
    id = 0
    review = dict()
    with open('nokia6610 (1).csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            row[0].strip()
            review[id] = row[0]
            id = id + 1

    # print(review)
    review = {key: list(map(str, value.split('but'))) for key, value in review.items()}
    
    with open('Aspect.csv') as aspect_file:
        readAspect = csv.reader(aspect_file, delimiter=',')
        for aspect in readAspect:
            if aspect[0] != "Group Name":
                aspect_dic[aspect[0]] = aspect[1]

    # print(aspect_dic["Battery"])
    
    aspect_dic = {key: list(map(str, value.split(','))) for key, value in aspect_dic.items()}
    
    aspect_sentence_dic = dict()
    # aspect_sentence_list_dic = {}
    
    for key,value in aspect_dic.items():
        aspect_sentence_list_dic = {}
        for word in value:
            for sentence_key, sentence_value in review.items():
                for l_value in sentence_value:
                    if word.lower() in l_value:
                        aspect_sentence_list_dic[sentence_key] = l_value

        aspect_sentence_dic[key] =  aspect_sentence_list_dic
        # print(aspect_sentence_dic["Speaker"])
        # aspect_sentence_list = []
    #print(aspect_sentence_dic["Sound Quality"])
    s = sentiment.SentimentAnalysis(filename='SentiWordNet.txt',weighting='geometric')
    score_aspectwise_dic = {}
    for key, value in aspect_sentence_dic.items():
        
        score_list = []
        for k, v in value.items():
            sentiments = s.score(v)
            score_list.append(sentiments)
        score_aspectwise_dic[key] = score_list
    #print(score_aspectwise_dic)
    opinion_dic = {}
    for key,value in score_aspectwise_dic.items():
        valence = []
        score = sum(value)/float(len(value))
        valence.append(score)
        pos = 0
        neg = 0
        for v in value:
            if v>0.0:
                pos+=1
            else:
                neg+=1
        pos_percent = (pos/float(len(value)))*100.0
        neg_percent = (neg/float(len(value)))*100.0
        valence.append(pos_percent)
        valence.append(neg_percent)
        opinion_dic[key] = valence
                
    print(opinion_dic)