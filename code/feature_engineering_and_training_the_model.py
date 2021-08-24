from sklearn.model_selection import train_test_split
import pandas as pd
import spacy
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.over_sampling import RandomOverSampler, SMOTE
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score
from sklearn.naive_bayes import MultinomialNB

muse = pd.read_csv('muse.csv')
queen = pd.read_csv('queen.csv')
df = pd.concat([muse, queen]).dropna()

X = df['Lyric']
y = df['Artist']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)

en = spacy.load('en_core_web_md')

def clean_my_string(lyric):
    """This function cleans the lyrical texts by running them through spacy"""
    clean_string = []
    lyric = lyric.lower()
    token_lyric = en(lyric) 
    for token in token_lyric:
        if not token.is_punct and not token.like_num:
            clean_string.append(token.text)
    return ' '.join(clean_string)

all_cleaned_lyrics = []
for lyric in tqdm(X_train):
    all_cleaned_lyrics.append(clean_my_string(lyric))

all_cleaned_test = []
for lyric in tqdm(X_test):
    all_cleaned_test.append(clean_my_string(lyric))

tf = TfidfVectorizer()

vectorized_lyrics= tf.fit_transform(all_cleaned_lyrics).todense()

readable_tf_vectors = pd.DataFrame(vectorized_lyrics, columns=tf.get_feature_names(), index=y_train)
X_train = readable_tf_vectors

tf_vectorized_test= tf.transform(all_cleaned_test).todense()

readable_tf_vectors_test = pd.DataFrame(tf_vectorized_test, columns=tf.get_feature_names(), index=y_test)
X_test = readable_tf_vectors_test

nb = MultinomialNB()
nb.fit(X_train,y_train)


def guess_the_artist():
    words = input('Please enter the lyrics \n')
    if words == '':
        print('You need to enter lyrics.')
        quit()
    words = [words]
    result = nb.predict(tf.transform(words))
    print(result, 'probably sang this.')
    

guess_the_artist()