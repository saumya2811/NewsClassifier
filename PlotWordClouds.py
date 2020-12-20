import pandas as pd
from imblearn.over_sampling import SMOTE
smote=SMOTE()
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
enc=LabelEncoder()
from wordcloud import WordCloud
hindu = pd.read_csv('data.csv')

#print(hindu.head())
def create_wordcloud(words):
    wordcloud=WordCloud(width=800, height=500, random_state=23, max_font_size=110).generate(words)
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
# #print(hindu.head(30))
# subset=hindu[hindu['Tag']=="Delhi"]
# #print(subset)
# text=subset.Body.values
# #print(text)
# words=' '.join(text)
# create_wordcloud(words)

