import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
enc=LabelEncoder()
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
smote=SMOTE()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

data=pd.read_csv('data.csv')

#######lable encoding to convert data into numerical values
#data['Title target']=enc.fit_transform(data['Title'])
data['Tag target']=enc.fit_transform(data['Tag'])
#data['Body target']=enc.fit_transform(data['Body'])
Y=data['Tag target']
X=data.loc[:,['Title', 'Body']]
#X=X.drop([0], axis=0)
#print(X.head(0))

#print(X.shape)


#######Split for training and Testing
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.3, random_state=8)
#print(X_train.shape)
data.to_csv("Processed_data.csv")
ngram_range=(1,2)
max_df=1.0
min_df=0
max_features=300
temp=X_train.head(5)
#print(X_train)
####Feature Extraction for Text
tfidf=TfidfVectorizer(encoding='utf8', ngram_range=ngram_range, stop_words=None, lowercase=False, max_df=max_df, min_df=min_df, max_features=205, norm='l2', sublinear_tf=True)
feature_train=tfidf.fit_transform(X_train['Body']).toarray()
#print(feature_train, tfidf.get_feature_names())
lable_train=Y_train
feature_test=tfidf.transform(X_test['Body']).toarray()
lable_test=Y_test


#######OverSampeling to Handle Sampeling Error
def smot(feature_train, lable_train):
    X_smote, Y_smote=smote.fit_sample(feature_train.astype('float'),lable_train)
    return X_smote, Y_smote
X_train,Y_train=smot(feature_train, lable_train)

###Naive Bayse
clf=GaussianNB()
clf.fit(X_train, Y_train)
clf_prediction= clf.predict(feature_test)
print("Accuracy", accuracy_score(lable_test, clf_prediction))
print(classification_report(lable_test, clf_prediction))

###Random Forest
clf=RandomForestClassifier(n_estimators=500)
clf.fit(X_train, Y_train)
clf_prediction= clf.predict(feature_test)
print("Accuracy", accuracy_score(lable_test, clf_prediction))
print(classification_report(lable_test, clf_prediction))

pickle.dump(clf, open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


