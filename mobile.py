import math, string, re, nltk
import csv
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
from collections import Counter


pos_tag_review = {}
bigrams_dic = {}
trigrams_dic = {}
aspect_opinion = {}
rule = {}
aspect_dic = dict()
not_list = ['no', 'nor', 'never', 'not', 'n\'t','don\'t',  'ain', 'aren', 'couldn', 'didn', 'doesn',
            'hadn', 'hasn', 'haven', 'isn', 'mightn', 'mustn', 'needn', 'shouldn', 'wasn', 'weren', 'won\'t', 'wouldn']

class sentiAnalyzer(object):

    # reading lexicon and creating dictionary
    lex = open('vader_lexicon.txt')

    count = 0
    lex_dic = dict()
    for l in lex:
        l.strip()
        (word, measure) = l.split('\t')[:2]
        lex_dic[word] = float(measure)

    # print(lex_dic)

    # reading review from dataset and splitting it and giving each review an id
    
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

    # checking the negation of the sentences
    # neg_sen_id = list()
    # for k, v in review.items():
    #     for l in v:
    #         for n in not_list:
    #             # print(n, v)
    #             if n == l:
    #                 neg_sen_id.append(k)
    #                 break
    # print(neg_sen_id)

    
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
    print(aspect_sentence_dic["Battery"])
    
    # Tokenize and POS Tag dictionary value

    tokenizer = RegexpTokenizer(r'\w+')
    # toker = tokenizer.tokenize('Eighty-seven miles to go, yet. Onward!')
    # print(toker)
    tokenize_review = {}

    for key, value in aspect_sentence_dic.items():
        token_dic = {}
        token_pos_tag = {}
        for l_key, l_value in value.items():
            list_str = ''.join(str(l_value))
            token = tokenizer.tokenize(list_str)
            token = [i for i in token if i not in stopwords.words('english')]
            token_pos_tag[l_key] = nltk.pos_tag(token)
            token_dic[l_key] = token

        tokenize_review[key] = token_dic
        pos_tag_review[key] = token_pos_tag

    # print(tokenize_review["Battery"])
    # print(pos_tag_review["Battery"])
    # print(set(tokenize_review.items()) & set(pos_tag_review.items()))
    # Bigram and Trigram

    for key, value in tokenize_review.items():
        bigrams_list = []
        trigrams_list = []
        bigrams = {}
        trigrams = {}
        for t_key,t_value in value.items():
            bigrams_list = ngrams(t_value,2)
            bigrams[t_key] = bigrams_list
            trigrams_list = ngrams(t_value,3)
            trigrams[t_key] = trigrams_list

        bigrams_dic[key] = bigrams
        trigrams_dic[key] = trigrams

    # print(bigrams_dic['Phone'])
    # print(*map(' '.join, bigrams_dic["Phone"][2]), sep=', ')
    rule_file = open('rule.txt')

    for r in rule_file:
        r = r.split()
        rule[r[0]] = r[1:]

    # print(rule)
    
    def check_Tag(v_bg, k, key):
        def rule_check(p):
            for k,r in rule.items():
                if p == r:
                    return k
        p = []

        for v in v_bg:
            for key_ps_tag, value_ps_tag in pos_tag_review.items():
                if key == key_ps_tag:
                    for k_ps_tag, v_ps_tag in value_ps_tag.items():
                        if k == k_ps_tag:
                            for tag in v_ps_tag:
                                if tag[0] == v:
                                    if tag[1] == 'NN' or tag[1] == 'NNS':
                                        f = 0
                                        for a_k, a_v in aspect_dic.items():
                                            for a_val in a_v:
                                                if a_val == tag[0]:
                                                    f = 1
                                        if f == 1:
                                            p.append(tag[1])
                                    else:
                                        p.append(tag[1])

        key_value = rule_check(p)
        if key_value == 'P1' or key_value == 'P4':
            aspect_opinion[v_bg[1]] = v_bg[0]
            # print(str(k)+':'+key)
        elif key_value == 'P3' or key_value == 'P9':
            aspect_opinion[v_bg[0]] = v_bg[1]
            # print(str(k)+':'+key)

    for key, bg_dic in bigrams_dic.items():
        for k, value in bg_dic.items():
            for v_bg in value:
                check_Tag(v_bg, k, key)

    # for key,value in aspect_opinion.items():
    #     print("Aspect: "+key+"------------Opinion: "+value)
                