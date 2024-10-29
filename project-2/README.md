# HW2 - Report
### Chris Skeens
### Due Date: 09/29/24

# Q1: 
*How many of your 500 URIs produced useful text? If that number was less than 500, did that surprise you*?
## Answer
Out of the 500 URIs processed, only 343 returned useful text. I was surprised that nearly half of the URIs collected returned no meaningful results. The most challenging part was selecting a word that could be found in 10 unique domains out of the remaining 343.

# Q2: 
*You must discuss in your report how you computed the values (especially IDF) and provide the formulas you used for TF, IDF, and TF-IDF.*
## Answer
Table 1. 10 Hits for the term "data", ranked by TF-IDF.
|TF-IDF	|TF	|IDF	|URI
|------:|--:|---:|---
|2.883	|0.097	|29.793	|https://www.linkedin.com/learning/topics/data-science?trk=homepage-basic_learning-cta
|2.554	|0.086	|29.793	|https://www.cnbc.com/
|0.801	|0.027	|29.793	|https://www.harvardonline.harvard.edu/
|0.428	|0.014	|29.793	|https://www.apply.vccs.edu/applications/vccs/apply.html?application_id=4096
|0.363	|0.012	|29.793	|https://gse.harvard.edu/
|0.159	|0.005	|29.793	|https://id.nbcnews.com/email-preferences?brand=nbc-news
|0.114	|0.004	|29.793	|https://www.nbcnews.com/pop-culture/pop-culture-news/nikocado-avocado-secret-weight-loss-rcna170142
|0.028	|0.001	|29.793	|https://finance.yahoo.com/personal-finance/find-best-cd-rates-165749654.html
|0.017	|0.001	|29.793	|https://www.nbcnews.com/news/nyc-running-clubs-dating-market-singles-apps-rcna167424
|0.017	|0.001	|29.793	|https://datasmart.hks.harvard.edu/addressing-native-homelessness-culturally-appropriate-housing

* Term Frequency (TF) was calculated by taking the total number of tokens that matched the search term, then dividing it by the total number of tokens found in the document.
* Inverse Document Frequency (IDF) was calculated by taking the size of Google's corpus and dividing it by the number of documents containing the search term.
* TF-IDF was calculated as the product of TF and IDF.
```
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
```

# Q3: 
*Briefly compare and contrast the rankings produced in Q2 and Q3.*
## Answer
Table 2.  10 hits for the term "data", ranked by PageRank of domain.
|PageRank	|URI
|-----:|---
|1.0    |	https://www.linkedin.com/
|0.8	|	https://gse.harvard.edu/
|0.8	|	https://id.nbcnews.com/
|0.8	|	https://www.nbcnews.com/ 
|0.8	|	https://www.nbcnews.com
|0.8	|	https://finance.yahoo.com
|0.7	|	https://www.harvardonline.harvard.edu/
|0.7	|	https://www.cnbc.com/
|0.7	|	https://datasmart.hks.harvard.edum
|0.5	|	https://www.apply.vccs.edu
|0.8	|	https://www.nbcnews.com

LinkedIn had the highest TF value out of the ten tested, which makes sense because it also scored the highest in PageRank. The most interesting results came from `https://www.apply.vccs.edu`. This page scored a higher TF but resulted in a low PageRank. This example shows that a page might have content highly relevant to the keyword searched for, but it is not widely recognized or linked to by other authoritative pages.

# Extra Credit
# Q5: 
The [inverted index](./inverted-index.txt) lists the number of documents containing each word instead of listing the filenames or URIs. This was done for readability. I used a dictionary to hold the key (word) and a set as the value, which contained all the filenames for the word. Using a set ensured that each word would only have a list of unique URIs. The most interesting thing is that my index ranked "the" as the third highest, instead of the highest. All other results in the index were as expected.
```
def build_inverted_index(word_index):
    with open("inverted-index.txt", 'w') as f:
        for key, value in sorted(word_index.items(), key=lambda item: len(item[1]), reverse=True):
            f.write('%s,%s\n' % (key, len(value)))
```