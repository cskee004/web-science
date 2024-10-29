import os
import random
import math
import pandas as pd
from textblob import TextBlob
from collections import defaultdict

word_index = defaultdict(set)
total_files = list()
TF_IDF = {}

occurence_in_doc = 0
words_in_doc = 0
total_documents = 0
relevant_documents = 0

def build_index():
    for name in os.listdir(r"./processed"):
        total_files.append(name)
        file_path = os.path.join(r"./processed", name)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read().lower()
            blob = TextBlob(text)
            for word in blob.words:
                if word not in word_index:
                    word_index[word].add(name)
                else:
                    word_index[word].add(name)

def search_index(w):
    for key, value in word_index.items():
        if w == key:
            search_results = list(value)
    return search_results

def get_random_10(final_list): 
    i = 0
    d = list()
    while i < 10:
        pick = random.choice(final_list)
        d.append(pick)
        i += 1
    return d

def compute_TF_IDF(d, t):
    for file_name in d:
        for name in os.listdir(r"./processed"):
            with open(os.path.join(r"./processed", name)) as f:
                if name == file_name:
                    print(f"Filename: {file_name}")
                    
                    text = f.read().lower()
                    blob = TextBlob(text)
                    
                    total_tokens = len(blob.words)
                    term_tokens = blob.words.count(t)
                    TF = term_tokens / total_tokens
                    
                    print(f"Occurences in doc {term_tokens}")
                    print(f"Words in doc {total_tokens}")
                    
                    total_documents = len(total_files)
                    total_google = 40000000000
                    relevant_documents = len(word_index.get(t))
                    #print(f"total docs in corpus {total_documents} / docs with term {relevant_documents}")
                    #print(f"total docs in google corpus {total_google} / docs with term {relevant_documents}")
                    #IDF_local = math.log2(total_documents / relevant_documents)
                    IDF = math.log2(total_google / relevant_documents)
                    TF_IDF = TF*IDF
                
                    rounded_TF = round(TF, 3)
                    rounded_IDF = round(IDF, 3)
                    rounded_TF_IDF = round(TF_IDF, 3)
                    print(f"TF: {rounded_TF}")
                    print(f"IDF: {rounded_IDF}")
                    print(f"TF-IDF: {rounded_TF_IDF}")
                    
    return 

w1 = "innovative" #19
w2 = "issues" #29
w3 = "data" #43 
w4 = "content" #52
w5 = "resources" #32

build_index()
search_results = search_index(w3)
compute_TF_IDF(search_results, w3)

def build_inverted_index(word_index):
    with open("inverted-index.txt", 'w') as f:
        for key, value in sorted(word_index.items(), key=lambda item: len(item[1]), reverse=True):
            f.write('%s,%s\n' % (key, len(value)))


