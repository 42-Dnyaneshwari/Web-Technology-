# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 08:35:34 2024

@author: Dnyaneshwari
"""
#Ensemble Techniques
#Random Forest
#confusion matrix when data is imbalace
import pandas as pd
from sklearn.datasets import load_digits
digits = load_digits()
dir(digits)

df=pd.DataFrame(digits.data)
df.head()
df['target']=digits.target
df[0:12]

X=df.drop('target',axis=1)
y=df.target

from sklearn.model_selection import train_test_split
#tain the data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=20)
#n_estimators is the no of trees in the random forest
model.fit(X_train,y_train)

model.score(X_train,y_train)
y_predicted=model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predicted)
cm

#Matplotlib Inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True)
plt.xlabel("Predicted")
plt.ylabel("Actual")



