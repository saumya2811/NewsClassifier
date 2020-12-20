
import pandas as pd
import string
import re
import nltk
#nltk.download('wordnet')
wn=nltk.WordNetLemmatizer()
stopwords=nltk.corpus.stopwords.words('english')
#print(stopwords[0:10])

data=pd.read_csv('data.csv')
data['Body']=data['Body'].replace("\n", '', regex=True)
data['Tag']=data['Tag'].replace("\n", '', regex=True)
data['Title']=data['Title'].replace("\n", '', regex=True)

###Removing Punctutions###
def remove_punc(txt):
    text_nopunct="".join([c for c in txt if c not in string.punctuation])
    return text_nopunct
data['Body']=data['Body'].apply(lambda x: remove_punc(x))


####Tokenization####
def tokenize(txt):
    tokens=re.split('\W+', txt)
    return tokens
data['Body']=data['Body'].apply(lambda x:tokenize(x.lower()))


####Removing Stop Words
def remove_sw(txt):
    txt_clean=[word for word in txt if word not in stopwords]
    return txt_clean
data['Body']=data['Body'].apply(lambda x: remove_sw(x))


###Lemmatization
def lemming(tokenized_text):
    text=[wn.lemmatize(word) for word in tokenized_text]
    return text
data['Body']=data['Body'].apply(lambda x: lemming(x))
print(data.head(5))
data.to_csv('data.csv')
data=pd.read_csv('data.csv')
print(data.head(5))


